# Superstore Sales Dashboard
An interactive Streamlit web application for exploring and visualizing sales and profit data from a Superstore dataset. Includes KPI metrics, bar charts, and filtering options.

# Features
Clean and preprocess the Superstore dataset

## Sidebar filters for:

Region selection

Product name selection

## Visual KPIs:

Total Sales

Total Profit

## Visualizations:

Top 5 Customers by Sales (Bar Chart)

Sales by Region (Bar Chart)

Profit by Category (Bar Chart)

View the filtered dataset in a tabular format

# Logging
The app logs key actions like:

Dropping unnecessary columns

Data loading status

Errors during file reading

Logs are printed in the terminal for easier debugging.

# Notes
The column "è®°å½•æ•°" in the dataset is renamed to "hello" and then dropped.

Columns like Ship.Date, Sub.Category, Order.Date, etc., are dropped to simplify analysis.

