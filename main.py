import pandas as pd

# Creating a DataFrame with some sample data
data = {
    'Name': ['Ivan', 'Olga', 'Pavlo', 'Nadiia', 'Andrii'],
    'Age': [28, 34, 29, 40, 23],
    'City': ['Kyiv', 'Lviv', 'Odessa', 'Kharkiv', 'Kyiv'],
    'Salary': [1500, 2200, 1800, 2400, 1700]
}

df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print("First few rows:")
print(df.head())

# Descriptive statistics for numerical columns
print("\nDescriptive statistics:")
print(df.describe())

# Select all rows where age is greater than 30
print("\nRows where age is greater than 30:")
over_30 = df[df['Age'] > 30]
print(over_30)

# Group by city and calculate the average salary
print("\nAverage salary by city:")
average_salary_by_city = df.groupby('City')['Salary'].mean()
print(average_salary_by_city)

# Adding a new column with a 10% salary increase
df['Salary_Increase'] = df['Salary'] * 1.1
print("\nDataFrame with new column (10% salary increase):")
print(df)

# Save the result to a CSV file
df.to_csv('output.csv', index=False)
print("\nDataFrame saved to 'output.csv'.")
