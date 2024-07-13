import pandas as pd

data = pd.read_csv('sample_data.csv')

data_filled = data.fillna(data.mean())
print(data_filled.head())
data_dropped = data.dropna()
print(data_dropped.head())
