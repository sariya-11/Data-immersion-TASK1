import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_dataset.csv")

# Show first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum()) 
print(df.columns)
# Bar Chart

df['City'].value_counts().plot(kind='bar')

plt.title("City Distribution")
plt.xlabel("City")
plt.ylabel("Count")

plt.show()
# Histogram
df['Purchase_Amount'].plot(kind='hist')
plt.title("Purchase Amount Distribution")
plt.xlabel("Purchase Amount")

plt.show()
# Heatmap

numeric_df = df.select_dtypes(include='number')

sns.heatmap(numeric_df.corr(), annot=True)

plt.title("Correlation Heatmap")

plt.show()