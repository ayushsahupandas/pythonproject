import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Department": ["IT", "HR", "IT", "HR"],
    "Salary": [50000, 40000, 60000, 45000]
}

df = pd.DataFrame(data)

# Filter
print(df[df["Salary"] > 45000])

# Group by
print(df.groupby("Department")["Salary"].mean())
