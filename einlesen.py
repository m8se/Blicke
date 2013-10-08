#! /usr/bin/env python 
from numpy import zeros
import pickle
datei=open("Daten/blick2.dat", "r")
#Daten werden Zeilenweise eingelsen und in einen 55X3X4510 Array verpackt. 55 entspricht der Dyaden Zahl. 3 fuer stressfrei, mit Stress und den Sonderfall. In die 4500 entspricht der maximalen Laenge.
id_lst=range(0)
zeitreihen=zeros([55,3,4510])
i=0
zeile=0
id_num_old=""
id_stelle=0
for line in datei:
	i+=1
	if (i>10000000)|(i==1):
		continue
	stelle=0
	id_num=""
	stress=""
	koordinate=0
	for zeichen in line:
		if (zeichen==chr(9))|(zeichen==' '):
			stelle+=1
			continue
		if stelle==1:
			id_num+=zeichen
		elif stelle==2:
			if id_num!=id_num_old:
				print zeile
				zeile=0
				#print id_num
				for i in range(len(id_lst)):
					if id_num==id_lst[i]:
						id_stelle=i
						#print "alt"
						break
				else:
					id_stelle=len(id_lst)
					id_lst.append(id_num)
				id_num_old=id_num
			stress=int(zeichen)
		elif (stelle==5):
			koordinate+=4*(int(zeichen)-1)
		elif (stelle==6):
			koordinate+=(int(zeichen)-1)
	if koordinate!='':
		#print int(koordinate)
		zeitreihen[id_stelle,stress-1,zeile]=koordinate+1
	zeile+=1
#Array mit den Daten und den Dyadennummern werden abgespeichert.
datei.close
speicher = open("Daten/id_lst.data", "w")
pickle.dump(id_lst[:],speicher)
speicher.flush()
speicher.close
speicher = open("Daten/zeitreihen.data", "w")
pickle.dump(zeitreihen[:],speicher)
speicher.flush()
speicher.close
