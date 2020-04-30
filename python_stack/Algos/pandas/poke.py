import pandas as pd
 
# DataFrame

df=pd.read_csv("./pandas/pokemon_data.csv")
print(df.head(3))
print(df.tail(3))
# all columns
print(df.columns)
# read each col
print(df[['Name','HP']])
# read a row - iloc
print(df.iloc[0])
print(df.iloc[0:4])
# read specific position - df.iloc[row,col]
print(df.iloc[1,2])
# print(df.loc[df['Type 1']=='Grass'])
print(df.describe())
print(df.sort_values(['Speed','Name'],ascending=False))
# first one asending and sec one descending
print(df.sort_values(['Name','Speed'],ascending=[1,0]))
df['total']=df["HP"]+df["Attack"]+df["Defense"]+df["Speed"]
print(df.head(5))

df=df.drop(columns=["total"])
print(df.head(5))
# add a col is diff way
df["Total"]=df.iloc[:4:10].sum(axis=1)
print(df.head(5))

# update df
cols=list(df.columns.values)
df=df[cols[0:4]+[cols[-1]]+cols[4:12]]
print(df.head(5))

df=df.groupby(["Name","Type 1"])
print(df)