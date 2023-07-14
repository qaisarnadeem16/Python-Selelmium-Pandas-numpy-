import pandas as pd

data = {
    'Employee': ['Nasir', 'Ali', 'Usama', 'Sophia', 'Adam', 'Mr Ishtiaq'],
    'Department': ['HR', 'Finance', 'HR', 'IT', 'Finance', 'IT'],
    'Salary': [5000, 6000, 4500, 8000, 5500, 6500]
}
df = pd.DataFrame(data)
grouped_df = df.groupby('Department')['Salary'].sum()

print(grouped_df)