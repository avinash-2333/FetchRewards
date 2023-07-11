import pandas as pd
import matplotlib.pyplot as plt import seaborn as sns
import numpy as np
%matplotlib inline
import pandas as pd
pd.options.display.float_format = '{:.2f}'.format

#Loading the data
data3 = pd.read_excel("brands.xlsx")


data3.info()

data3.head()

#Look for missing values
data3.isnull().sum()

#Percentage of null values for each variable that has missing values.
percentage_null_values= data3.isnull().mean()
for key,value in percentage_null_values.items():
    if value >0:
        print(key,":",value*100)


#Redundant records check
duplicateRowsDF = data3[data3.duplicated()]
print("Duplicate Rows except first occurrence based on all columns are :") 
print(duplicateRowsDF)

data3["category"].unique()

#Percentage of categorical values

freq_category = 100*(data3['category'].value_counts() / len(data3)) 
print(freq_category.map('{:,.2f} %'.format))


#Data quality issues found:

# Majority of brands belong to the 'Baking' category

# No data quality issues found except large number of missing values in topBrand and categoryCode columns.


