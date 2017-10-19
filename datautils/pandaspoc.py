import pandas as pd

results = {"ID":[10,11,12],"Name":["Anil","Rekha","Rishi"],"Age":[42,36,7]}

df = pd.DataFrame(results)
df.set_index("ID", inplace=True)

print(df)
print(df.Name.tolist())
print(df["Age"])
print(df[['Name','Age']])


csvFile = pd.read_csv("/development/python/poc/sampledata/ZILLOW-Z48168_ZRISFRR.csv")
csvFile.set_index("Date", inplace=True)
print(csvFile.head(10))
print(csvFile.tail())
