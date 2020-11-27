import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [10, 6]
plt.xlabel("Date")
plt.ylabel("Total Sales")

data = pd.read_csv(r"C:\Users\VAIBHAB\Desktop\Semester - 7\Big Data -2\Week-7\Project\data-set\BreadBasket_DMS.csv") 
data = data.replace(to_replace="NONE", value=np.nan).dropna()

data['Date'] = pd.to_datetime(data['Date'],format='%d-%m-%Y', errors='coerce')
data['year'] = data['Date'].dt.year

lol= data.loc[data['year'] == 2017]

# data with only item coffee
coffee= lol.set_index(['Item'])
onlycoffee= coffee.loc['Coffee']
onlycoffee.reset_index(inplace = True)

# display the dates with total transactions
popular=onlycoffee['Date'].value_counts()

print("\nTop 5 dates on which sales of coffee was highest: \n")
print("Date          Total")
print(popular.head())

popular.head().plot(kind='line', color='blue', marker='o')
plt.title("Top 5 sales day for coffee")
plt.show()

