import pandas as pd
groceries=pd.Series(data=[30,6,'Yes','No'],index=['eggs','apples','milk','bread'])
print(groceries)
print(groceries.values)
print(groceries.index)
groceries['bread']='Maybe'
for i,index in groceries.items():
    print(i,index)
print(groceries[['milk','bread']])
print("***")
print(groceries[[0,2]])

groceries.drop('milk',inplace=True)
print(f"After Drop {groceries}")