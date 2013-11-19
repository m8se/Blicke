# Skript zur Auswertung von Dyaden
# 	Darstellung des Cross Correlation Maximums


from pylab import *
import sys
from scipy.signal import argrelextrema
sys.path.append("../")
from hierarchische_clusterung import gruppen_erzeugen
from DAO import DAO

# Glaettung der Zeitreihe mit Moving Average
# a... Zeitreihe
# n=3, Mittelungslaenge
def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    return (ret[n - 1:] - ret[:1 - n]) / n

def find_global_maximum(cor,ARGS):
	if(ARGS):
		return cor.index(max(cor))
	else:
		return max(cor)

# Eine andere Methode, eine Einordnung durchzufuehren
def find_local_maximum(cor):
	N = 2
	avg = moving_average(cor, N);avg = avg[:len(avg) - N]
	
    # plot(avg)   Debugging
    
	# noch evt. Rauschen beruecksichtigen
	maxs = argrelextrema(avg, np.greater)[0]
	# for m in maxs:
	# 	plot(m,avg[m],'o')
	
	# Check for saddle points
	saddles = []
	saddle = 0
	for i in range(len(avg) - 1):
		if(avg[i] == avg[i + 1]):
			saddle += 1
		else:
			if(saddle != 0):
				saddles += [i - saddle / 2]
				saddle = 0

	# check if saddles should be maxima
	maxs = list(maxs)
	for s in saddles:
		print "Current saddle:" + str(s)
		index = s
		neg = True
		while(index > 0 and avg[index] == avg[s]):
			index -= 1
		if(avg[index] > avg[s]):
			neg = False
		index = s
		while(index < len(avg) - 1 and avg[index] == avg[s]):
			index += 1
		print s, index, avg[index], avg[s]

		if(avg[index] < avg[s] and neg):
			maxs += [s]
			print "New Maximum" + str(s)



	
	# Grenze bei len(avg)/2
	left = []
	right = []
	print "Maxima:" + str(maxs)
	for i in array(maxs):
		print i
		if(i > len(avg) / 2):
			right += [i]
		else:
			left += [i]
	if(len(right) > 0 and len(left) > 0):
		nleft = -max(array(left) - len(avg) / 2)
		nright = min(array(right) - len(avg) / 2)
		if(nright < nleft):
			res = nright
		else:	
			res = -nleft
	else:
		if(len(right) > 0):	
			res = min(array(right) - len(avg) / 2)
		elif(len(left) > 0):
			res = max(array(left) - len(avg) / 2)
		else:
			res = 100
	print res
	return res


# Start des Programms


dao = DAO()
ids = DAO.convertToList(sys.argv[1])
zeitreihen = dao.req_zeitreihen(ids, DAO.STRESS | DAO.NOT_STRESS)

dyade_num = len(ids)


def getMaximaFromDyads(ARGS):
	tau = 100
	maxs0 = []
	maxs2 = []

	for ind in range(len(zeitreihen)):
		figure(1)
		# Entferne alle Zustaende mit z<0 und z>16
		print "Dyade:" + str(ids[ind])
	
		zeitreihen_trimmed_m0 = []
		zeitreihen_trimmed_m2 = []
	
		for i in zeitreihen[ind, 0]:
			if(i > 0 and i < 17):  # wenn gueltiger Dyadenwert
				zeitreihen_trimmed_m0 += [i - 1]
		
		for i in zeitreihen[ind, 1]:
			if(i > 0 and i < 17):  # wenn gueltiger Dyadenwert
				zeitreihen_trimmed_m2 += [i - 1]
	
		# Berechnung der Kreuzkorrelation:
	
		if(len(zeitreihen_trimmed_m0) < tau * 2 + 1):
			tau = len(zeitreihen_trimmed_m0) / 2 - 1			
		cor0 = list(xcorr(array(zeitreihen_trimmed_m0) // 4, array(zeitreihen_trimmed_m0) % 4, maxlags=tau)[1])
		tau = 100
	
		if(len(zeitreihen_trimmed_m2) < tau * 2 + 1):
			tau = len(zeitreihen_trimmed_m2) / 2			
		cor2 = list(xcorr(array(zeitreihen_trimmed_m2) // 4, array(zeitreihen_trimmed_m2) % 4, maxlags=tau)[1])
	
		title("Cross Correlation von KuM vor Stress")
	
		# Finde das naechstliegende lokale Maximum
		print len(cor0)
	    
		# figure(2) #Debugging, um die Korrektheit des Optimierungsverfahrens zu testen
		maxs0 += [find_global_maximum(cor0,ARGS)]
		maxs2 += [find_global_maximum(cor2,ARGS)]
		if(ARGS):
			for i in range(len(maxs0)):
					maxs0[i]-=100
					maxs2[i]-=100
		return maxs0,maxs2
			


 
 # Problematisch hierbei sind fehlende Datenpunkte
 # Hiermit lassen sich Aussagen ueber die Entwicklung der Reaktionszeit zwischen ,Mutter und Kind machen
def clusterGlobalMaxima(ARGS):
	res=getMaximaFromDyads(ARGS)
	maxs0=res[0]
	maxs2=res[1]
	print maxs0
	
	fig = figure(3)
	xlabel("Maximum der Kreuzkorrelation vor Stress")
	ylabel("Maximum der Kreuzkorrelation nach Stress")
	plot(maxs0, maxs2, 'o')
	
	# Klassifiziere die Daten mit der HC Methode
	
	Maxs0 = array(maxs0)
	Maxs2 = array(maxs2)
	vector_list = zeros([len(Maxs0), 2])
	
	for k in range(len(Maxs0)):
		vector_list[k] = [Maxs0[k], Maxs2[k]]
	print vector_list
	groups = gruppen_erzeugen(vector_list)
	
	
	
	trimmed_groups = []
	
	
	# Erstelle richtige Gruppen, d.h. eliminiere hinten stehende -1
	for g in groups:
	    g_list = list(g)
	    try:
	        ind = g_list.index(-1)
	        trimmed_groups += [g[:ind]]
	    except:
	        trimmed_groups += [g]
	
	# Ordne die Gruppen alphabetisch
	ordered_groups = sorted(trimmed_groups, key=len)
	ordered_groups.reverse()
	
	print "Gruppen:", groups
	print "Trimmed Gruppen:", trimmed_groups
	print "Sorted Gruppen:", trimmed_groups
	
	
	# Zeige die 10 groessten Gruppen an
	N_max = 10  # maximal anzuzeigende Gruppen
	if(N_max > len(ordered_groups)):
	    N_max = len(ordered_groups)
	for g in range(N_max):
	    color = rand(3, 1)
	    for i in ordered_groups[g]:
	        scatter(maxs0[int(i)], maxs2[int(i)], s=g * 80, edgecolors=color, facecolors='none', linewidths=2, label='Class 2')
	
	for i in range(len(maxs0)):
	    text(maxs0[i], maxs2[i], ids[i])
	    
	    
	# Histogramme fuer die Stresstypen
	figure(4)
	subplot(211)
	xlabel("tau")
	ylabel("Abs. Haeufigkeit")
	title("Histogram der Cross Correlation Maxima vor Stress <max>="+str(mean(maxs0)))
	hist(maxs0,20)
	subplot(212)
	xlabel("tau")
	ylabel("Abs. Haeufigkeit")
	title("Histogram der Cross Correlation Maxima nach Stress <max>="+str(mean(maxs2)))
	hist(maxs2,20)
	
	
	show(fig)
	
	
clusterGlobalMaxima(True)
	


