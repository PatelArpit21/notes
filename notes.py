import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import parallel_coordinates

# Load dataset
df = pd.read_csv("supermarket_sales.csv")  # Replace with correct path if needed

# 1. First 8 rows
print("1. First 8 rows:")
print(df.head(8))

# 2. Check and fill missing values with mean
print("\n2. Missing values before filling:")
print(df.isnull().sum())
df.fillna(df.mean(numeric_only=True), inplace=True)
print("Missing values after filling:\n", df.isnull().sum())

# 3. Orders with Quantity < 3 and (Rating > 8.5 or Total > 600)
condition = (df['Quantity'] < 3) & ((df['Rating'] > 8.5) | (df['Total'] > 600))
num_orders = df[condition].shape[0]
print(f"\n3. Number of matching orders: {num_orders}")

# 4. Total purchase sum by Customer type
total_by_customer_type = df.groupby('Customer type')['Total'].sum()
print("\n4. Total purchase by Customer Type:")
print(total_by_customer_type)

# 5. % of gross income by Payment method
gross_income_by_payment = df.groupby('Payment')['gross income'].sum()
gross_income_percent = (gross_income_by_payment / gross_income_by_payment.sum()) * 100
print("\n5. Gross income percentage by Payment method:")
print(gross_income_percent)

# 6. Average purchase price by Gender
avg_total_by_gender = df.groupby('Gender')['Total'].mean()
print("\n6. Average purchase price by Gender:")
print(avg_total_by_gender)

# 7. Scatter plot: Total vs Rating
plt.figure(figsize=(8, 5))
plt.scatter(df['Total'], df['Rating'], marker='+', color='green', s=100)
plt.title('Total Amount Spent vs Rating')
plt.xlabel('Total Amount Spent')
plt.ylabel('Rating')
plt.grid(True)
plt.show()

# 8. Box plots for Rating and Quantity
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.boxplot(y=df['Rating'], color='lightblue')
plt.title("Rating Distribution")

plt.subplot(1, 2, 2)
sns.boxplot(y=df['Quantity'], color='lightcoral')
plt.title("Quantity Distribution")

plt.tight_layout()
plt.show()

print("\n8. Outlier analysis:")
print("- Look for dots beyond the whiskers in the box plots.")
print("- 'Rating' is between 4 and 10 mostly, any lower may be outlier.")
print("- 'Quantity' outliers might appear at very high or very low ends.")

# 9. Parallel Coordinates Plot
subset = df[['Product line', 'Unit price', 'Total', 'cogs']]
plt.figure(figsize=(12, 6))
parallel_coordinates(subset, class_column='Product line', colormap='viridis')
plt.title("Parallel Coordinates: Unit price, Total, COGS by Product line")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
