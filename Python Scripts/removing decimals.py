import numpy as np
import pandas as pd

df= pd.read_excel(r"E:\8th sem\FYP\Result1\FYP_model\bhawalpur.xlsx")



df['Maximum sustained wind speed']= df['Maximum sustained wind speed'].apply(np.ceil)
print(df)


#df['Meth Emis (KT)']= df['Meth Emis (KT)'].apply(np.ceil)
#print(df)

#df['NO emis (KT)']= df['NO emis (KT)'].apply(np.ceil)
#print(df)

#df['Flu  emis (KT)']= df['Flu  emis (KT)'].apply(np.ceil)
#print(df)

#df['Total GHG (KT)']= df['Total GHG (KT)'].apply(np.ceil)
#print(df)


df_result= df

df_result.to_excel(r"E:\8th sem\FYP\Result1\FYP_model\bhawalpurr.xlsx")

