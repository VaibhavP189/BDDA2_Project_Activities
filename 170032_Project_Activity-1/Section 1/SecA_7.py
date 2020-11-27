import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [10, 6]
plt.xlabel("Hours")
plt.ylabel("Total Sales")

data = pd.read_csv(r"C:\Users\VAIBHAB\Desktop\Semester - 7\Big Data -2\Week-7\Project\data-set\BreadBasket_DMS.csv") 
data = data.replace(to_replace="NONE", value=np.nan).dropna()


data['Time'] = pd.to_datetime(data['Time'],format='%H:%M:%S', errors='coerce')
# data['datetime'] = pd.to_datetime(data['Date']+" "+data['Time'])
data['hour'] = data['Time'].dt.hour

popular=data['hour'].value_counts()
print("\nNumber of sales per hour:  \n")
print(popular.sort_index())

# average=popular.sum()/24
# print("The number of average transactions per hour: " + str(average))

popular.sort_index().plot(kind='bar', color='blue')


plt.show()

