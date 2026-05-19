import pandas as pd
data ={
 'Name': ['Ali', 'Sara', 'John'],
 'Salary': [50000, 60000, 55000]
}

df = pd.DataFrame(data)

df["Salary_after_tax"]= df["Salary"] * 0.9

df.to_csv("output.csv", index=False)

print("ETL process completed")