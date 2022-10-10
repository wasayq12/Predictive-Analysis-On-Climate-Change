# importing libraries
import pandas as pd
import glob
import os
import csv

csv = {}
# merging the files
joined_files = os.path.join(r"", "accuweather*.csv")
fname = r"C:\Users\User\Desktop\scrapped\khi.csv"
  
# A list of all joined files is returned
joined_list = glob.glob(joined_files)
  
# Finally, the files are joined
df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
print(df)
df = pd.DataFrame([csv])

df.to_csv(fname, mode='a', header=True)