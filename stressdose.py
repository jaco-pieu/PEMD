import numpy as np 
import matplotlib.pyplot as plt 
from datetime import date 
import moy
import traitement

dispo="dispositif.txt"
taille0 =[]
taille1 = []
taille2 = []
taille3 = []
sources =["data1103.txt","data1403.txt","data1803.txt",
"data2103.txt","data2803.txt","data0504.txt"]
for i in sources: 
       moy0 = moy.moystressdose(1,0,i,dispo)
       taille0.append(moy0)
       moy1 = moy.moystressdose(1,1,i,dispo)
       taille1.append(moy1)
       moy2 = moy.moystressdose(1,2,i,dispo)
       taille2.append(moy2)
       moy3 = moy.moystressdose(1,3,i,dispo)
       taille3.append(moy3)


time = []
dates =[[2022,3,11],[2022,3,14],[2022,3,18],[2022,3,21],
[2022,3,28],[2022,4,5]]
for i in dates:
       day = traitement.days(i[0],i[1],i[2])
       time.append(day)
# Data for plotting
"""t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)"""

fig, ax = plt.subplots()
ax.plot(time, taille0, label = "dose 0")
ax.plot(time, taille1, label = "dose 20mg/l")
ax.plot(time, taille2, label = "dose 30mg/l")
ax.plot(time, taille3, label = "dose 40mg/l")

ax.set(xlabel='temps (jour)', ylabel='taille moyenne (cm)',
       title='Évolution de la taille moyenne des plants stressés et non stressés en fonction du temps')
ax.grid()
ax.legend()


daystress = traitement.days(2022,3,14)
ax.annotate('Début stress', xy=(daystress, 39), xytext=(daystress, 45),
            arrowprops=dict(facecolor='black', shrink=0.05))

daystress = traitement.days(2022,3,18)
ax.annotate('application ABA', xy=(daystress, 40.5), xytext=(daystress, 33),
            arrowprops=dict(facecolor='black', shrink=0.05))

fig.savefig("test.png")
plt.show()