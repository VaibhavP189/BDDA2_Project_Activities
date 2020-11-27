import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [10, 6]
plt.xlabel("Top Items sold")
plt.ylabel("Sales on Monday")

data = pd.read_csv(r"C:\Users\VAIBHAB\Desktop\Semester - 7\Big Data -2\Week-7\Project\data-set\BreadBasket_DMS.csv") 
data = data.replace(to_replace="NONE", value=np.nan).dropna()


data['Date1'] = pd.to_datetime(data.Date)
data['Day-of-Week'] = data['Date1'].dt.day_name()

# data['Date'] = pd.to_datetime(data['Date'])
# data['Day-of-Week'] = data['Date'].dt.day_name()

dat = data.set_index(['Day-of-Week'])
interval=dat.loc['Monday']
print(data)
popular=interval['Item'].value_counts()
print(popular.head())

mcolor = list('rgbkymc')
popular.head().plot(kind='bar', color=mcolor,width= .9)

plt.show()