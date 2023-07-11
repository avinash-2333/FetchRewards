import pandas as pd
import matplotlib.pyplot as plt import seaborn as sns
import numpy as np
%matplotlib inline
import pandas as pd
pd.options.display.float_format = '{:.2f}'.format

#Loading the data
data2 = pd.read_excel("receipts.xlsx")


data2.info()

data2.head()

#Look for missing values
data2.isnull().sum()

#Percentage of null values for each variable that has missing values.
percentage_null_values= data2.isnull().mean()
for key,value in percentage_null_values.items():
    if value >0:
        print(key,":",value*100)

data2["pointsEarned"].unique()

#Redundant records check
data2["_id/$oid"].unique()
data2["_id/$oid"].duplicated()


#Percentage of categorical values

freq_reasons = 100*(data2['bonusPointsEarnedReason'].value_counts() / len(data2)) 
print(freq_reasons.map('{:,.2f} %'.format))


#Data quality issues found:

# finishedDate- for 49%(almost half) of the receipts we don't know when do they become invalid.

# pointsEarned- 45% of the values for the 'pointsEarned' field are missing. If we look at the unique values for 'pointsEarned', we do not have a zero value. 

# purchasedItemCount- large number of missing values will pose problems for deciding if users who bought more than one unit of a product qualify for special offers/bonus points that require them to purchase certain amount of particular products/brands.

# totalSpent, rewardsReceiptItemList- Since data for these two fields is missing, it is natural that we don't have information about points earned(pointsEarned field) for those transactions.

