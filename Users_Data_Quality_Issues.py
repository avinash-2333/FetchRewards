import pandas as pd
import matplotlib.pyplot as plt import seaborn as sns
import numpy as np
%matplotlib inline
import pandas as pd
pd.options.display.float_format = '{:.2f}'.format

#Loading the data
data1 = pd.read_excel("users.xlsx")


data1.info()

data1["lastLoginDate"] = data1["lastLoginDate"].astype(str)

data1.head()

#Look for missing values
data1.isnull().sum()

#Percentage of null values for each variable that has missing values.
percentage_null_values= data1.isnull().mean()
for key,value in percentage_null_values.items():
    if value >0:
        print(key,":",value*100)


#Redundant records check
duplicateRowsDF = data1[data1.duplicated()] 
print(duplicateRowsDF)

#Unique values for categorical variables
data1["role"].unique()
data1["signUpSource"].unique()
data1["state"].unique()


#Data quality issues found:

# 1.More than half of the user records are redundant.

# 2.Small percentage of missing values in signUpSource and state columns