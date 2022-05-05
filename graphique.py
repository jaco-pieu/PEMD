import numpy as np 
import matplotlib.pyplot as plt 
from datetime import date 
import moy
import traitement

dispo="dispositif.txt"
taillepos =[]
tailleneg = []
sources =["data1103.txt","data1403.txt","data1803.txt",
"data2103.txt","data2803.txt","data0504.txt"]
for i in sources: 
       moypos = moy.moystress(1,i,dispo)
       taillepos.append(moypos)
       moyneg = moy.moystress(0,i,dispo)
       tailleneg.append(moyneg)

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
ax.plot(time, taillepos, label = "plants stressés",color = "r")
ax.plot(time, tailleneg, label = "plants non-stressés", color = "g")

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