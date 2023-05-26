import pandas as pd

name = pd.Series(['ali', 'atif', 'khalid'])
age = pd.Series([21, 25, 22])
designation = pd.Series(['Ceo', 'Manager', 'Developer'])

data = {'Name': name, 'Age': age, 'designation': designation }
print("Before Sort")
df = pd.DataFrame(data)
print(df)

print("Sorted by Age Ascending order")
df_sorted = df.sort_values(by='Age')

print("Sorted by Name Descending order")
df_sorted = df.sort_values(by='Name', ascending=0)

print(df_sorted)

print("Maximum Age")

maxAge = df['Age'].max()

maxAge_person = df[df["Age"] == maxAge]
print(maxAge_person)