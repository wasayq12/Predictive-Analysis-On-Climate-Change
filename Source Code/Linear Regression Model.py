import numpy as np
import pandas as pd
from sklearn import preprocessing 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import plotly.express as px

GCD= pd.read_excel(r"E:\7th sem\FYP\Temperature and Rainfall Datasets\Combined data\Clear Data\CompleteData.xlsx")
#print(GCD.head(5))
df_GCD= pd.DataFrame(GCD)
Intermediate_Set= df_GCD.iloc[:,0:9]
input_all_columns_GCD = Intermediate_Set.iloc[:,1:9]
input_all_columns_GCD.head(5)

print(df_GCD.isnull().values.any())

training_GCD, testing_GCD = train_test_split(input_all_columns_GCD, test_size=0.30, random_state=42)
print(training_GCD.shape)
print(testing_GCD.shape)

training_GCDdata = training_GCD.drop(["Average Temperature","Year"], axis=1)
print(training_GCDdata.shape)

training_GCDTemplabel = training_GCD["Average Temperature"]
print(training_GCDTemplabel)
'''
fig=plt.figure(figsize=(10,10))
plt.imshow(training_GCDdata.corr(), cmap=plt.cm.GnBu, interpolation='nearest',data=True)
plt.colorbar()
tick_marks = [i for i in range(len(training_GCDdata.columns))]
plt.xticks(tick_marks, training_GCDdata.columns, rotation=45)
plt.yticks(tick_marks, training_GCDdata.columns, rotation=45, size=8)
'''
training_GCD_relvantdata = training_GCDdata.drop(["Year"], axis=1)
'''
fig=plt.figure(figsize=(10,10))
plt.imshow(training_GCD_relvantdata.corr(), cmap=plt.cm.GnBu, interpolation='nearest',data=True)
plt.colorbar()
tick_marks = [i for i in range(len(training_GCD_relvantdata.columns))]
plt.xticks(tick_marks, training_GCD_relvantdata.columns, rotation=45)
plt.yticks(tick_marks, training_GCD_relvantdata.columns, rotation=45, size=8)
'''
lin_reg = LinearRegression()
lin_reg.fit(training_GCD_relvantdata, training_GCDTemplabel)

print("Coefficients: ", lin_reg.coef_)
print("Intercept: ", lin_reg.intercept_)

testing_GCDrelvantdata=testing_GCD.copy()
testing_GCDrelvantdata = testing_GCDrelvantdata.drop(["Average Temperature", "Year"], axis=1)
print(testing_GCDrelvantdata.shape)
testing_GCDTemplabel = testing_GCD["Average Temperature"]

print(testing_GCDTemplabel)
predict_temp = lin_reg.predict(testing_GCDrelvantdata)
print(predict_temp)
print(len(predict_temp))
print(lin_reg.score(testing_GCDrelvantdata, testing_GCDTemplabel))

actual_temp=list(testing_GCDTemplabel)
'''
fig=plt.figure(figsize=(10,10))x
plt.scatter(testing_GCD['Average Temperature'],predict_temp, color='red')
plt.plot(testing_GCD['Average Temperature'],actual_temp, color='blue')
'''
all_numerical_parameters = input_all_columns_GCD.drop(["Average Temperature","Year"], axis=1)
print(all_numerical_parameters.head(5))

predict_temp_Complete = lin_reg.predict(all_numerical_parameters)
print(predict_temp_Complete)
print(len(predict_temp_Complete))
'''
fig = plt.figure(figsize=(30,10))
fig = plt.scatter(all_numerical_parameters.index,input_all_columns_GCD["Average Temperature"], color='red', linewidths=1)
fig = plt.plot(all_numerical_parameters.index, predict_temp_Complete, color='blue', linewidth=1)
'''
GCD_2020=pd.read_excel(r'E:\7th sem\2020.xlsx')
print(GCD_2020.head(10))

GCD_2020["Day"] = pd.DatetimeIndex(GCD_2020["Date"]).day
GCD_2020["Month"] = pd.DatetimeIndex(GCD_2020["Date"]).month
print(GCD_2020.head(5))

evaluating_GCD_2020 = GCD_2020.drop(["Date","Average Temperature", "Year"], axis=1)
print(evaluating_GCD_2020.shape)
evaluating_GCDTemplabel = GCD_2020["Average Temperature"]
print(evaluating_GCDTemplabel)

print(lin_reg.score(evaluating_GCD_2020, evaluating_GCDTemplabel))

predict_2020 = lin_reg.predict(evaluating_GCD_2020)
print(predict_2020)
print(len(predict_2020))
'''
#fig=plt.figure(figsize=(18,12),facecolor = 'grey')
#plt.scatter(evaluating_GCD_2020.index,evaluating_GCDTemplabel, color='red', linewidths=5, alpha=1)
#plt.plot(evaluating_GCD_2020.index,predict_2020, color='blue', linewidth=2)
'''
'''
predict_2020=pd.DataFrame(predict_2020)
writer=pd.ExcelWriter(r"E:\7th sem\predicted2.xlsx")
predict_2020.to_excel(writer,'Sheet1')
writer.save()

#predict_2020.to_excel(r"E:\7th sem\predicted.xlsx")
'''