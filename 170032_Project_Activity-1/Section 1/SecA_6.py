import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [10, 6]
plt.xlabel("Week Days")
plt.ylabel("Total Items SOld")

data = pd.read_csv(r"C:\Users\VAIBHAB\Desktop\Semester - 7\Big Data -2\Week-7\Project\data-set\BreadBasket_DMS.csv") 
data = data.replace(to_replace="NONE", value=np.nan).dropna()

data['Date'] = pd.to_datetime(data['Date'],format='%d-%m-%Y', errors='coerce')
print(data)
data['Weekday'] = data['Date'].dt.weekday
data['Day'] = data['Date'].dt.day
# # data['datetime'] = pd.to_datetime(data['Date']+" "+data['Time'])
# # Year
# data['Year'] = data['Date'].apply(lambda x: x.split("-")[0])
# # Month
# data['Month'] = data['Date'].apply(lambda x: x.split("-")[1])
# # Day
# data['Day'] = data['Date'].apply(lambda x: x.split("-")[2])

sales = data['Weekday'].value_counts()
Rfinal = sales.sort_index()

Final = Rfinal.rename(index={0:'Monday',1:'Tuesday', 2:'Wednesday',3: 'Thursday', 4:'Friday', 5:'Saturday', 6: 'Sunday'})

print(Final)
# data.groupby('Weekday')['Item'].nunique().plot(kind='bar', title='Weekly Sales')
# print(data.groupby('Weekday')['Transaction'].nunique())

Final.plot(kind='line', color='red', marker = 'o')

plt.show()