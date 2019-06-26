# Reading an excel file using Python
import pandas as pd

#open MDP Extract
from pandas import ExcelWriter

data = pd.read_excel (r'\\CRSJBO-FS\UserData$\fmorales\Desktop\6.14 MDP Extract.xlsx')
df = pd.DataFrame(data)

#Filter by 1_AllStores
AllStores = df['Sale Loc:']=='1_AllStores'
All_S = df[AllStores]

#Filter by 2_30k & 15k
Ks = df['Sale Loc:']=='2_30k & 15k'
KsK = df[Ks]

#Filter by 1_AllStores
Exception = df['Sale Loc:']=='3_Exception'
Exc = df[Exception]

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


