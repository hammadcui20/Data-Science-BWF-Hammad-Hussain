import pandas as pd

data = pd.read_csv('sample_data.csv')
encoded_data = pd.get_dummies(data, columns=['Category'])
print(encoded_data.head())
