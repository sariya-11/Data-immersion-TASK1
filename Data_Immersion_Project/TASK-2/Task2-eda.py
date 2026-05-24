import pandas as pd

raw = pd.read_csv("raw_dataset.csv")
cleaned = pd.read_csv("cleaned_dataset.csv")

print(raw.describe())
print(cleaned.describe())

for col in raw.select_dtypes(include='object').columns:
    print(raw[col].value_counts().head())

for col in cleaned.select_dtypes(include='object').columns:
    print(cleaned[col].value_counts().head())
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

raw = pd.read_csv("raw_dataset.csv")
cleaned = pd.read_csv("cleaned_dataset.csv")

print("STARTING VISUALIZATION")

# 1. BAR CHART (LIMITED - NO LOOP ISSUE)

obj_cols = raw.select_dtypes(include='object').columns

if len(obj_cols) > 0:
    col = obj_cols[0]
    plt.figure()
    raw[col].value_counts().head(10).plot(kind='bar')
    plt.title(f"Bar Chart - Raw ({col})")
    plt.show()

# 2. HISTOGRAM

plt.figure()
raw.hist()
plt.suptitle("Histogram - Raw")
plt.show()

plt.figure()
cleaned.hist()
plt.suptitle("Histogram - Cleaned")
plt.show()

# 3. BOXPLOT

plt.figure()
raw.select_dtypes(include='number').plot(kind='box')
plt.title("Boxplot - Raw")
plt.show()

plt.figure()
cleaned.select_dtypes(include='number').plot(kind='box')
plt.title("Boxplot - Cleaned")
plt.show()

# 4. HEATMAP

plt.figure()
sns.heatmap(raw.corr(numeric_only=True), cmap="coolwarm")
plt.title("Heatmap - Raw")
plt.show()

plt.figure()
sns.heatmap(cleaned.corr(numeric_only=True), cmap="coolwarm")
plt.title("Heatmap - Cleaned")
plt.show()

print("VISUALIZATION DONE")
