import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_dataset.csv' with the actual file path of your CSV dataset
file_path = 'hotel_bookings.csv'

# Load the CSV into a Pandas DataFrame (assuming there's no header)
df = pd.read_csv(file_path, header=None)

# Display the first few rows of the DataFrame
print(df.head())

df.duplicated().sum() # -> 32020 duplicated rows
df.drop_duplicates(inplace = True)

missing_values = df.isnull().sum()
print("Missing values before handling:")
print(missing_values)
# Step 2: Handle Missing Values (examples)

# a. Removing rows with missing values
df.dropna(inplace=True)  # This will remove rows with any missing values

# b. Filling missing values with the mean for numeric columns
numeric_columns = df.select_dtypes(include=[int, float]).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# c. Filling missing values with a specific constant (e.g., 0)
# df.fillna(0, inplace=True)

# d. Interpolating missing values (useful for time series data)
# df.interpolate(inplace=True)

# After handling missing values, you may want to save the DataFrame to a new CSV file if needed.
# df.to_csv('cleaned_dataset.csv', index=False)

# Print the number of missing values for each column after handling
print("Missing values after handling:")
print(df.isnull().sum())

# Replace 'Hotel_Type_Column' with the actual column name from your dataset
df = pd.read_csv(file_path)


# Create a bar chart to visualize the distribution of hotel types
hotel_type_counts = df['hotel'].value_counts()

plt.figure(figsize=(8, 5))
hotel_type_counts.plot(kind='bar', color='green')
plt.title('Distribution of bookings in Hotel Types')
plt.xlabel('Hotel Type')
plt.ylabel('Bookings')
plt.xticks(rotation=0)
plt.show()


plt.figure(figsize=(8, 5))
plt.hist(df['lead_time'], bins=50, color='green')
plt.title('Distribution of Lead Times')
plt.xlabel('Lead Time (days)')
plt.ylabel('Bookings')
plt.show()