import pandas as pd

data1 = pd.read_csv('sample_data1.csv')
data2 = pd.read_csv('sample_data2.csv')
merged_data = pd.merge(data1, data2, on='ID')
print(merged_data.head())
