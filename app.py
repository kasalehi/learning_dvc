import pandas as pd 
import numpy as np

data={
    'Name':['Tom','nick','krish','jack'],
    'Age':[20,21,19,218]
}

df=pd.DataFrame(data)

path = 'data/output.csv'
df.to_csv(path, index=False)
