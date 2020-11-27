import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [10, 6]
plt.xlabel("Items")
plt.ylabel("Sales")

data = pd.read_csv(r"C:\Users\VAIBHAB\Desktop\Semester - 7\Big Data -2\Week-7\Project\data-set\BreadBasket_DMS.csv")

#Eliminating the Null Values and printing the top 10 selling items
data = data.replace(to_replace="NONE", value=np.nan).dropna()
Top = data['Item'].value_counts()
print("\nFrequency of Top 10 Selling Items: \n")
print(Top.head(10))

#Plot the chart of top 10 items
Top.head(10).plot(kind='bar', color='red')
plt.show()

