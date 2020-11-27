import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv(r"C:\Users\VAIBHAB\Desktop\Semester - 7\Big Data -2\Week-7\Project\data-set\BreadBasket_DMS.csv") 
# data = data.replace(to_replace="NONE", value=np.nan).dropna()

data= data.set_index(['Item'])
data= data.drop(['NONE'])
data.reset_index(inplace = True)

comb= data.loc[data['Item'] == 'Coffee', ['Transaction']]


new= data['Transaction'].isin(comb['Transaction'])
data['Item']=data[new]


newData= data.dropna()


newData= newData.set_index(['Item'])
newData= newData.drop(['Coffee'])
newData.reset_index(inplace = True)
print("\n Filtered Data set :\n")
print(newData)



popular=newData['Item'].value_counts()
Frequency= popular/len(newData)
print("\n Frequency of Items purchased with Coffee\n")
print(Frequency)

Frequency.head().plot(kind='bar',x='name',y='age')

print("\n \n Best item combination with coffee based on the frequency is bread Because it has been brought maximum number  times with Coffee. \n Cake, Tea, Pastry, Sandwich and medialuna can be consider good pairs with coffee because they are in the top 5 list of items transacted with coffee.\n \n")

plt.show()