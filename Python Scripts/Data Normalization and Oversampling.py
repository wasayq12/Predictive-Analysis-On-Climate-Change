import pandas as pd
from sklearn import preprocessing
import numpy as np
import scipy.stats as stats


#df = pd.read_excel(r"E:\8th sem\FYP\Factors Data\gaseszscore.xlsx")
dff = pd.read_excel(r"E:\8th sem\FYP\HM\quetta2010.xlsx")

#print(dff.info())
min_values = dff.min()
max_values = dff.max()

normalized_df = (dff - min_values) / (dff.max() - min_values)
#print(normalized_df.tail(10))
df_result= normalized_df

df_result.to_excel(r"E:\8th sem\FYP\HM\normalized2GHG.xlsx")

df = pd.read_excel(r"E:\8th sem\FYP\HM\normalized2GHG.xlsx")
#print(df.head())

dfa= df

dfa = pd.DataFrame({'x': np.random.random(100)*3, 'y': np.random.random(100) * 4 -2})
n = 365
new_values = pd.DataFrame({s: stats.rv_histogram(np.histogram(df[s])).isf(np.random.random(size=n)) for s in df.columns})
df = df.assign(data_type='original').append(new_values.assign(data_type='oversampled'))
#print(df.tail(7))
df_result2=df
df_result2.to_excel(r"E:\8th sem\FYP\HM\oversampled2GHG.xlsx")

df2 = pd.read_excel(r"E:\8th sem\FYP\HM\normalized2GHG.xlsx")

normalized_df=df2
#print(normalized_df.tail(7))

denormalized_df= normalized_df * (max_values - min_values) + min_values
print(denormalized_df.tail(7))
df_result3= denormalized_df
df_result3.to_excel(r"E:\8th sem\FYP\HM\denormalizedSIRFGHG.xlsx")

#df_result= denormalized_df
#df_result.to_excel(r"E:\8th sem\hmm.xlsx")
