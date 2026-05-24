import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

raw = pd.read_csv("raw_dataset.csv")
cleaned = pd.read_csv("cleaned_dataset.csv")

print("TASK 2 STARTED")

# DESCRIPTIVE STATISTICS
print(raw.describe())
print(cleaned.describe())

# HISTOGRAM
raw.hist(figsize=(10,5))
plt.show()

cleaned.hist(figsize=(10,5))
plt.show()

# BOX PLOT
raw.select_dtypes(include='number').plot(kind='box', figsize=(10,5))
plt.show()

cleaned.select_dtypes(include='number').plot(kind='box', figsize=(10,5))
plt.show()

# HEATMAP
plt.figure(figsize=(8,5))
#sns.heatmap(raw.corr(numeric_only=True), cmap="coolwarm")
#plt.show()

plt.figure(figsize=(8,5))
sns.heatmap(cleaned.corr(numeric_only=True), cmap="coolwarm")
plt.show()

print("TASK 2 COMPLETED")