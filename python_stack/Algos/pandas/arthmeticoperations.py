import pandas as pd
import numpy as np
x=pd.Series([10,6,2],["Apples","Banana","Kiwi"])
print(x["Apples"])
x+=1
print(x)
print(np.sqrt(x))
print(np.power(x,2))
