#! /usr/bin/env python
import pickle


def get_rel_auf(reqs,stress):
	daten=open("Daten/rel_aufenthalt.data", "r")
	rel_auf=pickle.load(daten)
	daten.close
	daten=open("Daten/id_lst.data", "r")
	id_lst=pickle.load(daten)
	daten.close
	stress_lst=[]
	for i in ([3,2,1,0]):
		if stress>=2**i:
			stress_lst.append(i)
			stress-=2**i
	ans=zeros([len(reqs)*len(stress_lst),18])
	req_it=0 #anzahl der bearbeiteten anfragen
	ans_it=0 #anzahl der bearbeiteten ids
	for req in reqs:
		id_nr=0
		for id in id_lst:
			if id=req:
				break
			id_nr+=1
		for stress in stress_lst:
			ans[ans_it,:16]=rel_auf[id_nr,stress,:]
			ans[ans_it,16:]=([req,stress])
	return ans[:]

def get_data(reqs,stress):
	daten=open("Daten/zeitreihen.data", "r")
	zeitreihen=pickle.load(daten)
	daten.close
	daten=open("Daten/id_lst.data", "r")
	id_lst=pickle.load(daten)
	daten.close
	stress_lst=[]
	for i in ([3,2,1,0]):
		if stress>=2**i:
			stress_lst.append(i)
			stress-=2**i
	stress_lst.reverse
	ans=zeros([len(reqs),len(stress_lst),4510])
	req_it=0 #anzahl der bearbeiteten anfragen
	ans_it=0 #anzahl der bearbeiteten ids
	for req in reqs:
		id_nr=0
		for id in id_lst:
			if id=req:
				break
			id_nr+=1
		for st in stress_lst:
			ans[ans_it,:]=zeitreihen[id_nr,st,:]
	return ans[:]
			
