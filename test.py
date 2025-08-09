import pandas as pd


df = pd.read_csv('PyQt/employees.csv')

print(df.iloc[0, 0])