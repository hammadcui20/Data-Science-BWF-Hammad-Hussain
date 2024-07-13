import pandas as pd

data = pd.read_csv('sample_data.csv')
pivot_table = data.pivot_table(values='Value', index='Category', columns='Subcategory', aggfunc='mean')
print(pivot_table)
