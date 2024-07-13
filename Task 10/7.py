import pandas as pd

data = pd.read_csv('sample_data.csv')
grouped_data = data.groupby('Category').mean()
print(grouped_data)
