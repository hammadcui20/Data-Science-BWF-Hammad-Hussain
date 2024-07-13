import pandas as pd

data = pd.read_csv('sample_data.csv')
data_cleaned = data.drop_duplicates()
print(data_cleaned.head())
