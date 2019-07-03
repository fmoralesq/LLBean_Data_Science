from tkinter import filedialog
import pandas as pd

data1 = pd.read_excel(r'\\CRSJBO-FS\UserData$\fmorales\Desktop\07.02 MDP.xlsx')
df1 = pd.DataFrame(data1)

df_new = df1[['IMD_ID','Item ID','TOT_STORE QTY','Desc Review / Submit','Sale Loc:','Sale Date:','End Date','PRICE POINT','MD Type (1st, 2nd, 2+)']]
print(df_new)

