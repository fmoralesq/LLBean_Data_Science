# Reading an excel file using Python
import pandas as pd

#open MDP Extract and Ref Info
from pandas import ExcelWriter

data1 = pd.read_excel (r'\\CRSJBO-FS\UserData$\fmorales\Desktop\6.14 MDP Extract.xlsx')
df1 = pd.DataFrame(data1)

data2 = pd.read_excel (r'\\CRSJBO-FS\UserData$\fmorales\Desktop\Reference_Info.xlsx')
df2 = pd.DataFrame(data2)

#Join between Data Frames
df_cd = pd.merge(df2, df1, on='IMD_ID',how='left')

print(df_cd)