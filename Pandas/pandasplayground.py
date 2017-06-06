import numpy as np
import pandas as pd

data = {'Company':['GOOGLE','GOOGLE','MSFT','MSFT','FACEBOOK','FACEBOOK'],
'User':['Sam','Mikie','Amy','Vanessa','Malburg','Richo'],
'Sales':[200,300,150,110,100,100]}

df = pd.DataFrame(data)
# print(df)

byComp = df.groupby('Company')
 
print(byComp.mean())