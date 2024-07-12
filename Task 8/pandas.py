import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

print("Mean Age:", df['Age'].mean())
print("Cities:", df['City'].unique())

print("People older than 30:\n", df[df['Age'] > 30])
