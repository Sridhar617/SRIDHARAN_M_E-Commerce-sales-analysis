import pandas as pd

import matplotlib.pyplot as plt



# File path to the Amazon sale report CSV

file_path = '/content/Amazon Sale Report.csv'



# Read the CSV file with improved error handling

try:

    data = pd.read_csv(file_path, on_bad_lines='warn', encoding='utf-8', quotechar='"', escapechar='\\')

    print(f"Columns in CSV: {data.columns.tolist()}")  # Check columns to ensure proper loading

except Exception as e:

    print(f"Error reading the CSV file: {e}")

    exit()  # Exit the program if the file can't be loaded



# Check the first few rows of the dataset to understand its structure

print(data.head())



# If necessary, rename the columns to match the expected ones

# Adjust column names as per your actual CSV structure

column_mapping = {

    'OrderID': 'OrderID',  # Change this if the actual name is different

    'Product': 'Product',  # Change this if the actual name is different

    'Quantity': 'Quantity',  # Change this if the actual name is different

    'Price': 'Price',  # Change this if the actual name is different

    'CustomerID': 'CustomerID',  # Change this if the actual name is different

    'Date': 'Date'  # Change this if the actual name is different

}



# Rename the columns (if necessary)

data = data.rename(columns=column_mapping)



# Ensure the necessary columns exist after renaming

required_columns = ['OrderID', 'Product', 'Quantity', 'Price', 'CustomerID', 'Date']

missing_columns = [col for col in required_columns if col not in data.columns]

if missing_columns:

    print(f"Missing columns: {missing_columns}")

else:

    # Add a new column for TotalPrice

    data['TotalPrice'] = data['Quantity'] * data['Price']

    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')  # Convert to datetime and handle invalid dates



    # 1. Calculate total sales

    total_sales = data['TotalPrice'].sum()

    print(f"Total Sales: ${total_sales:.2f}")



    # 2. Identify best-selling products

    best_selling_products = data.groupby('Product')['Quantity'].sum().sort_values(ascending=False)

    print("\nBest-Selling Products:")

    print(best_selling_products.head(5))



    # 3. Analyze customer purchase patterns

    customer_sales = data.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False)

    print("\nTop 5 Customers by Total Spend:")

    print(customer_sales.head(5))



    # 4. Generate visualizations



    # Top 5 best-selling products (Bar chart)

    plt.figure(figsize=(10, 5))

    best_selling_products.head(5).plot(kind='bar', color='teal')

    plt.title('Top 5 Best-Selling Products')

    plt.xlabel('Product')

    plt.ylabel('Total Quantity Sold')

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()



    # Sales trend over time (Line plot for daily sales)

    daily_sales = data.groupby(data['Date'].dt.date)['TotalPrice'].sum()

    plt.figure(figsize=(12, 6))

    daily_sales.plot(kind='line', marker='o', linestyle='-')

    plt.title('Daily Sales Trend')

    plt.xlabel('Date')

    plt.ylabel('Total Sales ($)')

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()
