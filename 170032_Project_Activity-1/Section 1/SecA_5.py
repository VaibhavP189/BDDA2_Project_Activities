import pandas as pd
import numpy as np
import seaborn as sns   
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [10, 6]
plt.xlabel("Months")
plt.ylabel("Total Items SOld")

data = pd.read_csv(r"C:\Users\VAIBHAB\Desktop\Semester - 7\Big Data -2\Week-7\Project\data-set\BreadBasket_DMS.csv") 
data = data.replace(to_replace="NONE", value=np.nan).dropna()


data['Date'] = pd.to_datetime(data['Date'],format='%d-%m-%Y', errors='coerce')
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day



Sales = data['Month'].value_counts()
Rfinal = Sales.sort_index()

Final = Rfinal.rename(index={1:'January',2:'Febrary', 3:'March',4: 'April', 5:'May', 6:'June', 7: 'July',8:'August', 9:'September',10: 'October', 11:'November', 12:'December'})

Final.plot(kind='bar', title='Monthly Sales')

plt.show()