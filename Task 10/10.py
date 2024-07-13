import pandas as pd

data = pd.read_csv('sample_data.csv')
selected_data = data[['Category', 'Value']]
print(selected_data.head())
