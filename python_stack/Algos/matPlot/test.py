#%%
import matplotlib as plt
import numpy as np
import pandas as pd
import seaborn as sb

# %matplotlib inline
poke=pd.read_csv('./matPlot/pokemon_data.csv')
print(poke.shape)
print(poke.head(10))
sb.countplot(data=poke,x='Generation')




# %%
