import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import os
import logging

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class EDA:
    def __init__(self):
        self.file = None

    def clean(self):
        file_path = r"D:\Bilal folder\internship\task5\superstore.csv"
        if os.path.isfile(file_path):
            try:
                self.file = pd.read_csv(file_path)
                # Rename incorrect column
                self.file.rename(columns={"è®°å½•æ•°": "hello"}, inplace=True)

                # Drop unnecessary columns if they exist
                columns_to_drop = ["hello", "Ship.Date", "Sub.Category", "Market2", "weeknum", "Order.Date", "Row.ID"]
                for col in columns_to_drop:
                    if col in self.file.columns:
                        self.file.drop(columns=col, inplace=True)
                        logging.info(f"Dropped column: {col}")

                logging.info("Data cleaned successfully.")
            except Exception as e:
                logging.error(e)

    def get_data(self):
        return self.file


class StreamApp(EDA):
    def app(self):
        st.title("Superstore Sales Dashboard")
        st.markdown("Explore sales data with dynamic filters and KPIs")

        df = self.get_data()

        if df is not None:
            # Sidebar filters
            st.sidebar.header("Filter Data")
            region_filter = st.sidebar.multiselect("Select Region(s)", df["Region"].unique(), default=df["Region"].unique())
            category_filter = st.sidebar.multiselect("Select Category(s)", df["Product.Name"].unique(), default=df["Product.Name"].unique())

            # Apply filters
            filtered_df = df[
                (df["Region"].isin(region_filter)) &
                (df["Product.Name"].isin(category_filter))
            ]

            if filtered_df.empty:
                st.warning("No data available for selected filters.")
                return

            # KPI Calculations
            total_sales = filtered_df["Sales"].sum()
            total_profit = filtered_df["Profit"].sum()
            top_customers = filtered_df.groupby("Customer.Name")["Sales"].sum().sort_values(ascending=False).head(5)

            # Display KPIs
            st.subheader("Key Performance Indicators")
            col1, col2 = st.columns(2)
            col1.metric("Total Sales", f"${total_sales:,.2f}")
            col2.metric("Total Profit", f"${total_profit:,.2f}")

            # Bar chart - Top 5 Customers
            st.subheader("Top 5 Customers by Sales")
            if not top_customers.empty:
                fig1, ax1 = plt.subplots()
                top_customers.plot(kind='bar', ax=ax1, color='skyblue')
                ax1.set_ylabel("Sales")
                ax1.set_xlabel("Customer")
                ax1.set_title("Top 5 Customers by Sales")
                st.pyplot(fig1)
            else:
                st.info("No customers found for selected filters.")

            # Region-wise Sales
            region_sales = filtered_df.groupby("Region")["Sales"].sum()
            st.subheader("Sales by Region")
            if not region_sales.empty:
                fig2, ax2 = plt.subplots()
                region_sales.plot(kind="bar", color="orange", ax=ax2)
                ax2.set_title("Sales by Region")
                st.pyplot(fig2)
            else:
                st.info("No regional sales data available.")

            # Category-wise Profit
            cat_profit = filtered_df.groupby("Product.Name")["Profit"].sum()
            st.subheader("Profit by Category")
            if not cat_profit.empty:
                fig3, ax3 = plt.subplots()
                cat_profit.plot(kind="bar", color="green", ax=ax3)
                ax3.set_title("Profit by Category")
                st.pyplot(fig3)
            else:
                st.info("No category profit data available.")

            # Show filtered DataFrame
            st.write("Filtered Data", filtered_df)

        else:
            st.error("Data not loaded. Please check the file path.")



app = StreamApp()
app.clean()
app.app()
