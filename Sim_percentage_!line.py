import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Calculate the similarity percentage for each pair of strings and store in the 3rd column
df['SimilarityPercentages'] = df.apply(lambda row: [
    round((sum(c1 == c2 for c1, c2 in zip(row['col1'], row2['col2'])) / max(len(row['col1']), len(row2['col2']))) * 100, 2)
    for _, row2 in df.iterrows()
], axis=1)

# Create a new column with formatted similarity percentages
df['SimilarityPercentage'] = df['SimilarityPercentages'].apply(lambda x: ', '.join(map(str, x)))

# Drop the 'SimilarityPercentages' column
df.drop(columns=['SimilarityPercentages'], inplace=True)

# Save the DataFrame back to the same CSV file
df.to_csv('data.csv', index=False)

print(df)
