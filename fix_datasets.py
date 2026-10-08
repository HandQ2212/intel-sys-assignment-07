import pandas as pd

# Fix Diabetes
df_dia = pd.read_csv('data/diabetes.csv')
# The notebooks expect numeric data and an 'Outcome' column.
# Let's create 'Outcome' based on glyhb > 6.5
df_dia['Outcome'] = (df_dia['glyhb'] > 6.5).astype(int)
# Drop non-numeric columns and na
df_dia = df_dia.select_dtypes(include=['number']).fillna(0)
df_dia.to_csv('data/diabetes.csv', index=False)
print("Fixed diabetes.csv")

# Fix Housing
df_hou = pd.read_csv('data/vietnam_housing_dataset.csv')
df_hou = df_hou.rename(columns={
    'Area': 'Diện tích',
    'Bedrooms': 'Số phòng ngủ',
    'Bathrooms': 'Số phòng vệ sinh',
    'Price': 'Giá'
})
# Convert these columns to numeric if they aren't already, handle errors
for col in ['Diện tích', 'Số phòng ngủ', 'Số phòng vệ sinh', 'Giá']:
    if col in df_hou.columns:
        df_hou[col] = pd.to_numeric(df_hou[col], errors='coerce')

df_hou.to_csv('data/vietnam_housing_dataset.csv', index=False)
print("Fixed vietnam_housing_dataset.csv")

