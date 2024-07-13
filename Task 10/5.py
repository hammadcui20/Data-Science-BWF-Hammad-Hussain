import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv('sample_data.csv')
scaler = MinMaxScaler()
normalized_data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
print(normalized_data.head())
