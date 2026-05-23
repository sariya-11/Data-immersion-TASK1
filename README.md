# Data Immersion Task 1 - Data Cleaning & Wrangling Project:

# Objective:
The main objective of this project is to understand raw data and convert it into a clean, structured, and analysis-ready format using Python.
This includes identifying data issues, fixing them, and creating useful new features for better insights.

# Dataset Description:
The dataset used in this project is a sample customer sales dataset. 
It contains information such as:
   - Customer details (ID, Name, Gender, City)
   - Date of Birth (DOB)
   - Purchase information (Amount, Date)

This dataset helps in analyzing customer behavior and spending patterns.

# Data Quality Issues Identified:
During initial analysis, the following issues were found:
  - Missing values in City and Purchase Amount columns
  - Duplicate records in dataset
  - Inconsistent text formatting (Gender column)
  - Unstructured date formats

# Data Cleaning Steps Performed:
To solve these issues, the following steps were performed:

   - Loaded dataset using **Pandas**
   - Checked missing values and duplicate records
   - Removed duplicate entries
   - Filled missing values using appropriate methods (mean / "Unknown")
   - Standardized text fields (e.g., Gender formatting)
   - Converted date columns into proper datetime format
   - Handled incorrect or missing date values

# Feature Engineering:
To improve the dataset, new meaningful features were created:

   - **Customer_Age** → Calculated using Date of Birth
   - **Spending_Category** → Classified customers as High or Low based on purchase amount

# Output:
After cleaning and transformation, the final dataset was saved as:

    [`cleaned_dataset.csv`]

This dataset is now clean, structured, and ready for further analysis or visualization.

# Tools & Technologies Used:
- Python. 
- Pandas.
- NumPy.
- Visual Studio Code.


# Outcome:
This project helped in understanding real-world data problems and how to clean and prepare data for analysis. 
It also improved skills in Python data handling and preprocessing techniques.
