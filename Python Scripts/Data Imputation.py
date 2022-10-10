import numpy as np
import pandas as pd
import os

df= pd.read_excel(r"E:\8th sem\FYP\Temperature and Rainfall Datasets\Lahore 2010-2018\LahoreCombined.xlsx")

#print(df['Minimum temperature'].isnull().head(10))
#print(df.head(10))
print(df.isnull().sum())
#MEAN MEDIAN
'''
df['Minimum temperature'].fillna(df['Minimum temperature'].median(), inplace=True)
df['Average Temperature'].fillna(df['Average Temperature'].median(), inplace=True)
df['Maximum temperature'].fillna(df['Maximum temperature'].median(), inplace=True)
df['Atmospheric pressure at sea level'].fillna(df['Atmospheric pressure at sea level'].median(), inplace=True)
df['Average relative humidity'].fillna(df['Average relative humidity'].median(), inplace=True)
df['Total rainfall'].fillna(df['Total rainfall'].median(), inplace=True)
'''
#LINEAR INTERPOLATION


df['Rainfall'].interpolate(method='linear', direction = 'forward', inplace=True) 
print(df.head(10))

#df['Sea level'].interpolate(method='linear', direction = 'forward', inplace=True) 
#print(df['Sea level'].head(10))
df_result= df

#df['Sea level'].fillna(df['Sea level'].median(), inplace=True)
#print(df['Sea level'].tail(10))
# saving the excel
df_result.to_excel(r"E:\8th sem\FYP\lahoree.xlsx")


print(df.isnull().sum())
