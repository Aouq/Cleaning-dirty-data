import pandas as pd

df = pd.read_csv('dirty data.csv')

# Clean the column names
# Observe from debugger column names have \xa0 instead of space
df.columns = df.columns.str.replace('\xa0', ' ')
df.columns = df.columns.str.strip()

# Get rid of columns with missing data
df = df.drop(columns = ['Peak', 'All Time Peak', 'Ref.'])

# Change 2022 to 2024 in adjusted gross
df.columns = df.columns.str.replace('2022', '2024')

# Select all columns containing strings
string_columns = df.select_dtypes(include = ['object']).columns

# Cleaning data within string columns
for col in string_columns:
    # Replace anything in [], this must be done first so the next line doesn't strip []
    df[col] = df[col].str.replace(r'\[.*\]', '', regex = True)

    # Replace other messy texts
    df[col] = df[col].str.replace(r'[^\w\s\–]', '', regex = True)

    # Replace extra spaces
    df[col] = df[col].str.replace(r'\s+', ' ', regex = True)

# Turn strings into numbers
for col in ['Actual gross', 'Adjusted gross (in 2024 dollars)', 'Average gross']:
    df[col] = pd.to_numeric(df[col])


df.to_excel('python_cleaned.xlsx', index = False)
