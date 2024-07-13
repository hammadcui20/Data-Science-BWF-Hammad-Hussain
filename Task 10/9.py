import pandas as pd

data = pd.read_csv('sample_data.csv')
filtered_data = data[data['Value'] > 10]
print(filtered_data.head())
