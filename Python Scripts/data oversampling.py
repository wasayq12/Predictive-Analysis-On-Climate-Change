import pandas as pd
import scipy.stats as stats
import numpy as np

df = pd.read_excel(r"E:\8th sem\FYP\Pressuredata\quetta.xlsx")
dfa= df

dfa = pd.DataFrame({'x': np.random.random(100)*3, 'y': np.random.random(100) * 4 -2})
n = 365
new_values = pd.DataFrame({s: stats.rv_histogram(np.histogram(df[s])).isf(np.random.random(size=n)) for s in df.columns})
df = df.assign(data_type='original').append(new_values.assign(data_type='oversampled'))
print(df.tail(7))
df_result= df
df_result.to_excel(r"E:\8th sem\FYP\Pressuredata\gasesoversampled.xlsx")

