import pandas as pd

df = pd.read_csv('data.csv', index_col='region_name')
df.info()


df.drop(['1', '2'], inplace=True)
df.sort_values('salary', inplace=True)

print(df.head(6).tail(1))
print(df.head(49).tail(1))
print(df.head(51).tail(1))

print(df['salary'].mean())
print(df['salary'].median())