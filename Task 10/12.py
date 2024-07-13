import pandas as pd

data1 = pd.read_csv('sample_data1.csv')
data2 = pd.read_csv('sample_data2.csv')
concatenated_data = pd.concat([data1, data2], axis=0)
print(concatenated_data.head())
