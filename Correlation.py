import csv
import numpy as np
import matplotlib.pyplot as plt
data=open('istherecorrelation.csv')
datacsv = csv.reader(data, delimiter = ';')

datacsv_list=list(datacsv)
headers = datacsv_list.pop(0)

years=[]
WO=[]
Beers=[]
for i in datacsv_list:
    years.append(float(i[0]))
    WO.append(float(i[1].replace(',','')))
    Beers.append(float(i[2]))
    
Beers_norm=np.array(Beers)/max(Beers)
WO_norm=np.array(WO)/max(WO)
plt.plot(years,WO_norm, label=headers[0])
plt.plot(years,Beers_norm, label=headers[1])
plt.title('Normalized beer consumption and WO (2006-2018)')
plt.savefig('Correlation_plot')
plt.legend()
plt.show()

