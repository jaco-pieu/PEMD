from datetime import date

def importdata(datatitle):
	fichier = open(datatitle, 'r')
	nligne = 0
	for i in fichier:
	    nligne+=1
		
	#print(nligne)
	fichier.close()

	k = 0
	data=[ [0 for j in range(8)] for i in range(8)]
	fichier = open(datatitle, 'r')
	for i in range(nligne):
		val = fichier.readline()
		if val == "\t\t\t\t\t\t\t\t\n":
			pass
		else:

			val = val.replace(",",".").replace("\t\t",",")
			val = val.replace("\t",",").replace("\n","")
			val = val.split(",")
			for j in range(8):
			    #print(val[j])
			    data[k][j] = float(val[j])

			k+=1
	    
	fichier.close()
	return data


def days(year,mons,da):
	d0 =date(2022,2,21)
	d1 =date(year,mons,da)
	delta = d1-d0
	days = delta.days
	return days

#print(days(2022,2,22))