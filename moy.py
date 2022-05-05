import traitement

def moystress(stress,datatitle,dispotitle):
	dispo = traitement.importdata(dispotitle)
	data = traitement.importdata(datatitle)

	nbr = 0
	somme = 0
	for i in range(8):
		for j in range(8):
			etat = str(dispo[i][j])[2]
			if etat == str(stress):
				somme = somme + data[i][j]
				nbr+=1
			else:
				pass
	moy = somme/nbr

	return moy


#print(moystress(1,"data.txt","dispositif.txt"))

def moydose(dose,datatitle,dispotitle):
	dispo = traitement.importdata(dispotitle)
	data = traitement.importdata(datatitle)

	nbr = 0
	somme = 0
	for i in range(8):
		for j in range(8):
			etat = str(dispo[i][j])[1]
			if etat == str(dose):
				somme = somme + data[i][j]
				nbr+=1
			else:
				pass
	moy = somme/nbr

	return moy

def moystressdose(stress,dose,datatitle,dispotitle):
	dispo = traitement.importdata(dispotitle)
	data = traitement.importdata(datatitle)

	nbr = 0
	somme = 0
	for i in range(8):
		for j in range(8):
			etat = str(dispo[i][j])[2]
			dodose = str(dispo[i][j])[1]
			if etat == str(stress) and dodose == str(dose):
				somme = somme + data[i][j]
				nbr+=1
			else:
				pass
	moy = somme/nbr

	return moy


def moybloc(bloc,datatitle,dispotitle):
	dispo = traitement.importdata(dispotitle)
	data = traitement.importdata(datatitle)

	nbr = 0
	somme = 0
	for i in range(8):
		for j in range(8):
			etat = str(dispo[i][j])[0]
			if etat == str(bloc):
				somme = somme + data[i][j]
				nbr+=1
			else:
				pass
	moy = somme/nbr

	return moy