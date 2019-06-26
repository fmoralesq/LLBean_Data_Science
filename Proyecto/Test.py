# Reading an excel file using Python
import pandas as pd

#open MDP Extract
data = pd.read_excel (r'\\CRSJBO-FS\UserData$\fmorales\Desktop\6.14 MDP Extract.xlsx')
df = pd.DataFrame(data)

#Filter by 1_AllStores
AllStores = df['Sale Loc:']=='1_AllStores'
All_S = df[AllStores]
print(All_S)

#Create File with filtered values
All_S.to_excel(r'\\CRSJBO-FS\UserData$\fmorales\Desktop\MDP Extract_Test.xlsx',sheet_name='Sheet1')
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


