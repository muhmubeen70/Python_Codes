from difflib import SequenceMatcher

import Levenshtein
import matplotlib.pyplot as plt
import pandas as pd

file_path = 'TCSV.csv'
df = pd.read_csv(file_path)


def similarity_calculate(str1, str2):
    max_length = max(len(str1), len(str2))
    distance = Levenshtein.distance(str1, str2)
    similarity_ratio = (max_length - distance) / max_length
    return similarity_ratio*100

percentages = []
count = {}
# for word1, word2 in product(df['1'], df['2']):
for word1 in df['1']:
    for word2 in df['2']:
        similarity_percentage = round(similarity_calculate(word1, word2),2)
        percentages.append(similarity_percentage)
        count[similarity_percentage] = count.get(similarity_percentage, 0) + 1
# print((count.items()))
count_df = pd.DataFrame(list(count.items()), columns=['Similarity', 'Frequency'])
similarity_df = pd.DataFrame(percentages, columns=['Similarity'])
merge_df = pd.concat([df, similarity_df], axis=1)

merge_df.to_csv('final_result.csv', index=False)
print(count_df)

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
plt.bar(count_df['Similarity'], count_df['Frequency'])
plt.xlabel('Similarity')
plt.ylabel('Frequency')
plt.title('Plot')
plt.xticks(rotation=90)
plt.tight_layout()

plt.subplot(1, 2, 2)
plt.pie(count_df['Frequency'], labels=count_df['Similarity'], autopct='%1.1f%%')
plt.title('Similarity Percentage Distribution')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

plt.show()