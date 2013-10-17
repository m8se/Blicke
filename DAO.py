import pickle
from numpy import zeros

class DAO:
    NOT_STRESS=1;
    UNSED=2;
    STRESS=4;
    
    def __init__(self):
        self.f=open("Daten/zeitreihen.data");
        self.zeitreihen=pickle.load(self.f)
        self.f.close();
        
        self.f=open("Daten/rel_aufenthalt.data")
        self.rel_auf=pickle.load(self.f)
        self.f.close();
        
        self.f=open("Daten/id_lst.data")
        self.id_lst=pickle.load(self.f)
        self.f.close();
        print
        
        
        print "Init"
    
    def req_rel_auf(self,reqs,stress):    
        self.stress_lst=[]
        for i in ([3,2,1,0]):
            if stress>=2**i:
                self.stress_lst.append(i)
                stress-=2**i
            self.ans=zeros([len(reqs)*len(self.stress_lst),18])
            self.req_it=0 #anzahl der bearbeiteten anfragen
            self.ans_it=0 #anzahl der bearbeiteten ids
            for req in reqs:
                self.id_nr=self.id_lst.index(str(req))
            for self.stress in self.stress_lst:
                self.ans[self.ans_it,:16]=self.rel_auf[self.id_nr,self.stress,:]
                self.ans[self.ans_it,16:]=([req,self.stress])
                return self.ans[:]
                    
    def req_zeitreihen(self,reqs,stress):
        self.stress_lst = []
        for i in ([3, 2, 1, 0]):
            if stress >= 2 ** i:
                self.stress_lst.append(i)
                stress -= 2 ** i
        self.stress_lst.reverse
        self.ans = zeros([len(reqs), 4510])
        self.req_it = 0  # anzahl der bearbeiteten anfragen
        self.ans_it = 0  # anzahl der bearbeiteten ids
        for req in reqs:
            self.id_nr=self.id_lst.index(str(req))
            for st in self.stress_lst:
                self.ans[self.ans_it, :] = self.zeitreihen[self.id_nr, st, :]
                self.ans_it+=1
        return self.ans[:]
    