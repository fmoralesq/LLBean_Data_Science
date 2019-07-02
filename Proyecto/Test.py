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

#Filter by 1_AllStores
AllStores = df_cd['Sale Loc:']=='1_AllStores'
All_S = df_cd[AllStores]

#Filter by 2_30k & 15k
Ks = df_cd['Sale Loc:']=='2_30k & 15k'
KsK = df_cd[Ks]

#Filter by 1_AllStores
Exception = df_cd['Sale Loc:']=='3_Exception'
Exc = df_cd[Exception]

#Create File with filtered values
writer = ExcelWriter(r'\\CRSJBO-FS\UserData$\fmorales\Desktop\MDP Extract_Test.xlsx')
All_S.to_excel(writer,'Sheet1')
KsK.to_excel(writer,'Sheet2')
Exc.to_excel(writer,'Sheet3')
writer.save()

#Query a usar


'''
Select distinct
IMD_ID,
ITEM_ID,
PROD_ID,
ITEM_DESC,
MERC_DSCRPTR_DESC,
MERC_DSCRPTR_ID
from 
DSS.PROD_REF
where 
PROD_DEL_FLG = 'N'
and IMD_ID in (XXXXXX,
'''


