import pandas as pd
import numpy as np

# LOAD DATASET
df = pd.read_csv('raw_dataset.csv')

print("ORIGINAL DATA:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# CLEANING
df = df.drop_duplicates()

df['City'] = df['City'].fillna('Unknown')

df['Gender'] = df['Gender'].astype(str).str.upper()

df['Purchase_Amount'] = df['Purchase_Amount'].fillna(df['Purchase_Amount'].mean())

df['DOB'] = pd.to_datetime(df['DOB'], errors='coerce')

df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'], errors='coerce')

df['Customer_Age'] = pd.Timestamp.now().year - df['DOB'].dt.year

df['Spending_Category'] = np.where(df['Purchase_Amount'] > 500, 'High', 'Low')

df.to_csv('cleaned_dataset.csv', index=False)

print("\nDONE ✔ CLEANING COMPLETE")