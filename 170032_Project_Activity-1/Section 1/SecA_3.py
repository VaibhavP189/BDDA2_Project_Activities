import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [10, 6]
plt.xlabel("Top Items sold")
plt.ylabel("Sales in 2017")

data = pd.read_csv(r"C:\Users\VAIBHAB\Desktop\Semester - 7\Big Data -2\Week-7\Project\data-set\BreadBasket_DMS.csv") 
data['Date1'] = pd.to_datetime(data.Date)
data['year'] = data['Date1'].dt.year

# #Eliminating the null values.
data = data.replace(to_replace="NONE", value=np.nan).dropna()


NewItems= data.loc[data['year'] == 2017]

popular=NewItems['Item'].value_counts()
print("Top 5 Items sold in 2017: \n")
print(popular.head())

# #Plot the Graph for the derived dataset.
popular.head().plot(kind='bar', color='red')
plt.show()