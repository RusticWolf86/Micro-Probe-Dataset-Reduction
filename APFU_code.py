#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from molmass import Formula

# Read the CSV file into a DataFrame
df = pd.read_excel('/home/ghost/Documents/Sunit_Sir_Work/Apatite.xlsx')

# Function to calculate molecular weights
calculate_molecular_weight = lambda column_name: Formula(column_name).mass

# Create a new DataFrame with values divided by molecular weights
ap_df = pd.DataFrame({column: df[column] / calculate_molecular_weight(column) for column in df.columns})

# Edit column names in the new DataFrame
ap_df.columns = [column.split('O')[0].rstrip('0123456789') for column in ap_df.columns]
ap_df['P'] *= 5

# Create a new DataFrame with additional columns
new_df = ap_df.copy()
new_df['Total'] = new_df.sum(axis=1)
new_df['Oxy'] = (new_df['F'] + new_df['Cl']) / 2
new_df['Cor'] = new_df['Total'] - new_df['Oxy']
new_df['Final'] = 26 / new_df['Cor']

# Create a new DataFrame with values multiplied by the 'Final' column
final_df = new_df.drop(['Total', 'Oxy', 'Cor'], axis=1)  # Exclude unnecessary columns
final_df = final_df.mul(new_df['Final'], axis=0)
final_df = final_df.drop(['Final'], axis=1)

# Print the DataFrames
print("Original DataFrame:")
print(df)
print("\nProcessed DataFrame:")
print(new_df)
print("Final DataFrame:")
print(final_df)

new_df.to_excel('/home/ghost/Documents/Sunit_Sir_Work/AP.xlsx')
final_df.to_excel('/home/ghost/Documents/Sunit_Sir_Work/APFU.xlsx')


# In[ ]:




