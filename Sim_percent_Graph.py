import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('TCSV.csv')

# Calculate the similarity percentage for each pair of strings and store in the 3rd column
df['SimilarityPercentages'] = df.apply(lambda row: [
    round((sum(c1 == c2 for c1, c2 in zip(row['1'], row2['2'])) / max(len(row['1']), len(row2['2']))) * 100, 2)
    for _, row2 in df.iterrows()
], axis=1)

# Create a new column with formatted similarity percentages
df['SimilarityPercentage'] = df['SimilarityPercentages'].apply(lambda x: ', '.join(map(str, x)))

# Drop the 'SimilarityPercentages' column
df.drop(columns=['SimilarityPercentages'], inplace=True)

# Plot a bar chart
similarity_counts = df['SimilarityPercentage'].str.split(', ', expand=True).stack().value_counts()
plt.figure(figsize=(12,5))
plt.subplot(1, 2, 1)
plt.bar(similarity_counts.index, similarity_counts)
plt.title('Distribution of Similarity Percentages (Bar Chart)')
plt.xlabel('Similarity Percentage')
plt.ylabel('Count')
# plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Plot a pie chart

plt.subplot(1, 2, 2)
plt.pie(similarity_counts, labels=similarity_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Similarity Percentages (Pie Chart)')
plt.axis('equal')
plt.show()

print(df)
