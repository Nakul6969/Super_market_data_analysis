import pandas as pd

df = pd.read_excel("superstore.xls")

#Exploring DATASET
print("Shape : ",df.shape)
print(df.head()) #First five rows
print(df.tail()) #Last five rows
print(df.describe()) #Numeric decription

#Handling Missing Values
print("Missing : ",df.isnull().sum())

#Removing duplicate values
df = df.drop_duplicates()

#Sorting
df.sort_values(by=['Sales','Profit'] , ascending = False , inplace=True)

#Aggregation
print(df.groupby("Category")["Sales"].sum())
print(df.groupby("State")["Profit"].mean())






