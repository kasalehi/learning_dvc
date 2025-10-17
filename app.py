import pandas as pd 
import numpy as np

data={
    'Name':['Tomy','nicky','krishy','jack'],
    'Age':[22,22,12,215]
}

df=pd.DataFrame(data)

path = 'data/output.csv'
df.to_csv(path, index=False)
