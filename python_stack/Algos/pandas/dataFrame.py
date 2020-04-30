import pandas as pd
items={'Bob':pd.Series([1,2,3],["bike","shirt","tie"]),'Monika':pd.Series([5,2,1],["top","earrings","car"])
}
shopping_cart=pd.DataFrame(items)
# like a spreadsheet
# union - col- keys
print(shopping_cart)

items2={'Bob':pd.Series([1,2,3]),'Monika':pd.Series([5,2,1])
}
shopping_list2=pd.DataFrame(items2)
print(shopping_list2)
print(shopping_cart.shape)
bob_shopping_cart=pd.DataFrame(items,columns=["Bob"])
print(bob_shopping_cart)

# ****************
items=[{'bike':10,'pants':20,'watches':30},{'cups':10,'tray':20,'cool':23}]
store_items=pd.DataFrame(items,index=['store1','store2'])
store_items['bike']=[2,5]
store_items['pants']=[12,20]
# top 2 rows
print(store_items.head(2))
# bottom 2 rows
print(store_items.tail(2))

