import traitement

fichiersortie = "sortie.txt"
data = traitement.importdata("data2803.txt")
dispo = traitement.importdata("dispositif.txt")
stress = []
dose = []
bloc = []
val = []

for i in range(0,8):
    for j in range(0,8):
        id = dispo[i][j]
        id = str(id)
        stress.append(id[2])
        dose.append(id[1])
        bloc.append(id[0])
        val.append(data[i][j])

sortie = open(fichiersortie , "w")
sortie.write("stress \t dose \t bloc \t valeur \n")
for i in range(0,64):
    da = str(stress[i]) + "\t" + str(dose[i]) + "\t" + str(bloc[i]) + "\t" + str(val[i]) + "\n"
    sortie.write(da)
sortie.close()