from scipy.stats import zscore
import pandas as pd
import scipy.stats as stats


# Create a sample df
df = pd.read_excel(r"E:\8th sem\GHG data\monthly.xlsx")
# Calculate the zscores and drop zscores into new column

#print(df.head())

print(df.info())
#df['Average Temperature zscore'] = stats.zscore(df['Average Temperature'])
#print(df.head())

df = df.select_dtypes(include='number').apply(stats.zscore)
print(df.head())

df_result= df
df_result.to_excel(r"E:\8th sem\GHG data\gaseszscore.xlsx")


