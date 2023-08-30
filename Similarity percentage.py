import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('TCSV.csv')

# Calculate the similarity percentage for each pair of strings and store in a new column
df['SimilarityPercentages'] = df.apply(lambda row: [
    round((sum(c1 == c2 for c1, c2 in zip(row['col1'], row2['col2'])) / max(len(row['col1']), len(row2['col2']))) * 100, 2)
    for _, row2 in df.iterrows()
], axis=1)

# Save the DataFrame back to the same CSV file
df.to_csv('TCSV.csv', index=False)

print(df)
