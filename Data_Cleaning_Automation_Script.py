# Data Cleaning Automation

#------------------------------------------------------------------------
#%%
# ## Step 1: Automating Missing Values Handling with Python Functions
import pandas as pd

# Define a reusable function to handle missing values
def handle_missing_values(df, method='mean', fill_value=None):
    if method == 'drop':
        return df.dropna()
    elif method == 'fill':
        return df.fillna(fill_value)
    elif method == 'mean':
        numerical_cols = [col for col in df.columns if df[col].dtype in ['int64', 'float64']]

        # for col in df.columns: 
        #     if df[col].dtype in ['int64', 'float64']:
        #         numerical_cols = col

        print(f"numerical_cols: {numerical_cols}")

        df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())
        return df
    else:
        raise ValueError("Invalid method provided")

# Example dataset
data = {'Name': ['Alice', 'Bob', None, 'David'],
        'Age': [25, None, 30, 22],
        'Salary': [50000, 60000, None, 45000]}
df = pd.DataFrame(data)

# Use the function to handle missing values by filling with the mean
cleaned_df = handle_missing_values(df, method='mean')
print(cleaned_df)

#------------------------------------------------------------------------
#%%
##Step 2: Removing Duplicates Efficiently

# Define a function to remove duplicates based on specific columns
def remove_duplicates(df, subset=None):
    return df.drop_duplicates(subset=subset)

# Example dataset with duplicates
data = {'Name': ['Alice', 'Bob', 'Alice', 'David'],
        'Age': [25, 30, 25, 22],
        'Salary': [50000, 60000, 50000, 45000]}
df = pd.DataFrame(data)

# Remove duplicates based on the 'Name' column
cleaned_df = remove_duplicates(df, subset=['Name'])
print(cleaned_df)

#------------------------------------------------------------------------
#%%
## Step 3: Transforming Data Types in a Pipeline

# Define a function to transform data types
def transform_data_types(df, col_types):
    for col, dtype in col_types.items():
        df[col] = df[col].astype(dtype)
    return df

# Example dataset with incorrect data types
data = {'Name': ['Alice', 'Bob', 'David'],
        'Age': ['25', '30', '22'],
        'Salary': ['50000', '60000', '45000']}
df = pd.DataFrame(data)

# Specify the correct data types
col_types = {'Age': 'int', 'Salary': 'float'}

# Apply the transformation
cleaned_df = transform_data_types(df, col_types)
print(cleaned_df.dtypes)

#------------------------------------------------------------------------
#%%
##Step 4: Building an Automated Data Cleaning Pipeline
import pandas as pd

# Define a function to handle missing values
def handle_missing_values(df, method='mean', fill_value=None):
    if method == 'mean':
        # Convert numeric columns to float first to avoid errors
        for col in df.select_dtypes(include=['object', 'string']).columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        df = df.fillna(df.mean(numeric_only=True))
    elif method == 'median':
        df = df.fillna(df.median(numeric_only=True))
    elif method == 'mode':
        df = df.fillna(df.mode().iloc[0])
    elif method == 'constant' and fill_value is not None:
        df = df.fillna(fill_value)
    return df

# Define a function to remove duplicates
def remove_duplicates(df, subset=None):
    df = df.drop_duplicates(subset=subset)
    return df

# Define a function to transform data types
def transform_data_types(df, col_types):
    for col, dtype in col_types.items():
        df[col] = df[col].astype(dtype)
    return df

# Build a complete data cleaning pipeline
def data_cleaning_pipeline(df, missing_values_method='mean', fill_value=None, subset=None, col_types=None):
    # Handle missing values
    df = handle_missing_values(df, method=missing_values_method, fill_value=fill_value)
    
    # Remove duplicates
    df = remove_duplicates(df, subset=subset)
    
    # Transform data types
    if col_types:
        df = transform_data_types(df, col_types)
    
    return df

# Example dataset with various issues
data = {'Name': ['Alice', 'Bob', None, 'Alice'],
        'Age': ['25', None, '30', '22'],
        'Salary': [50000, 60000, None, 50000]}

df = pd.DataFrame(data)

# Define data types and run the pipeline
col_types = {'Age': 'int', 'Salary': 'float'}
cleaned_df = data_cleaning_pipeline(df, missing_values_method='mean', subset=['Name'], col_types=col_types)

print(cleaned_df)
print("\nData Types:")
print(cleaned_df.dtypes)

#----------------------------------------------------------------------
# %%
