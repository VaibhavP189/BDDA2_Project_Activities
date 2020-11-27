import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [10, 6]
plt.xlabel("Week Days")
plt.ylabel("Sales")

data = pd.read_csv(r"C:\Users\VAIBHAB\Desktop\Semester - 7\Big Data -2\Week-7\Project\data-set\BreadBasket_DMS.csv") 
data = data.replace(to_replace="NONE", value=np.nan).dropna()

bread= data['Item']== 'Bread'
bread_data= data[bread]

bread_data['Date'] = pd.to_datetime(data['Date'],format='%d-%m-%Y', errors='coerce')
bread_data['weekday'] = bread_data['Date'].dt.weekday
sales=bread_data['weekday'].value_counts()
new= sales.sort_index()
renamed= new.rename(index={0:'Monday',1:'Tuesday', 2:'Wednesday',3: 'Thursday', 4:'Friday', 5:'Saturday', 6: 'Sunday'})

print("\nBreads sold per weekday: \n")

print(renamed)

average=renamed.sum()/7
print("\nThe number of average transactions of bread per weekday: " + str(average)+ "\n")

renamed.plot(kind='line', color='red', marker='o')

plt.show()


