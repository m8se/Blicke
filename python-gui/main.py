from Tkinter import *
import pickle
import time
import tkFont 
from numpy.distutils.exec_command import exec_command

class App:
    
    list;
    
    def getCurrentStress(self):
        curSel=self.v.get()
        if(curSel==1):return DAO.NOT_STRESS
        elif(curSel==2):return DAO.STRESS
        elif(curSel==3):return DAO.STRESS|DAO.NOT_STRESS
        elif(curSel==4): return 8
        
    def init_popup(self,root):
        
        self.popup = Menu(root, tearoff=0)
        self.popup.add_command(label="Diagramm",command=self.showDyad) # , command=next) etc...
        self.popup.add_command(label="XCorr",command=self.showXCorr)
        self.popup.add_separator()
        self.popup.add_command(label="Home")
    
    
    def getSelectedDyads(self):
        print "IDs: "+str(self.ids)
        cur_sel=self.list.curselection();
        cur_ids=[]
        for i in cur_sel:
            cur_ids+=[int(self.ids[self.ids_len-1-int(i)])]
        print cur_ids;
    def getSelectedPopupDyad(self):
        return self.ids[self.ids_len-1-self.cur]
    def selectAll(self):
        self.list.selection_set(0,END)
    def showClusterProb(self):
        print "getSelectedDyads():",self.getSelectedDyads()
        exec_command("cd ..;python gruppen_darstellen.py '"+str(self.getSelectedDyads())+"' "+str(self.getCurrentStress()))
    def showClusterStaytime(self):
        exec_command("cd ..;python staytime.py")
    def showClusterCorr(self):
        exec_command("cd ../correl;python correl.py "+str(self.ids[self.cur])+" "+self.getCurrentStress())
    def showClusterXCorrAll(self):
        exec_command("cd ..;python xcorrel_all.py")
    def showDyad(self):
        print "Aktuellle Dyade: "+str(self.getSelectedPopupDyad())
        exec_command("cd ..;python vis_dyade.py "+str(self.ids[self.cur]))
    def showXCorr(self):
        exec_command("cd ..;python xcorrel.py "+str(self.ids[self.cur]))
    def do_popup(self,event):
        # display the popup menu 
        self.cur=self.list.nearest(event.y)
        print self.cur
        self.popup.tk_popup(event.x_root, event.y_root,1)
                
    def party(self,event):
            print "Hallo"
    
    def __init__(self,master):
        # Alle Dyandennr. einlesen
        
        f=open("../Daten/zeitreihen.data");
        zeitreihen=pickle.load(f)
	f.close()
        #print zeitreihen

        dyade_num=len(zeitreihen)
        f=open("../Daten/id_lst.data");
        self.ids=pickle.load(f)
        self.ids_len=len(self.ids)
	f.close()
        
        # Aufbau der GUI
        
        frame=Frame(master)
        frame.pack(fill=BOTH,expand=1)
        
        f1=Frame(frame)
        f1.pack(pady=20)
        
        
        l=Label(f1,text="Bitte waehlen Sie die auswertenden Dyaden:")
        f = tkFont.Font(l,("Sans Serif",12))
        l.configure(font=f)
        l.pack()
        
        f2=Frame(frame)
        f2.pack(fill=BOTH,expand=1)
        
        f3=LabelFrame(f2,text="Dyadenauswahl")
        f3.pack(side=LEFT,fill=BOTH)
        
        b_reset=Button(f3,text="Alles auswaehlen",command=self.selectAll)
        b_reset.pack(fill=BOTH)
        
        f4=Frame(f3)
        f4.pack(fill=BOTH,expand=1)
        scrollbar=Scrollbar(f4,orient=VERTICAL) 
        self.list=Listbox(f4,font=("Arial", 10),yscrollcommand=scrollbar.set,selectmode=MULTIPLE,selectbackground="lightblue",selectforeground="white")
        scrollbar.config(command=self.list.yview)
        for item in self.ids:
            self.list.insert(0,"Dyade "+item)
        self.list.pack(fill=Y,side=LEFT)
        scrollbar.pack(side=LEFT,fill=Y)
        
        #Entry(f2,textvariable=text).grid(row=0,column=1)
        #self.current=self.list.curselection()
        #self.poll()
        
        f7=Frame(f3)
        f7.pack(fill=BOTH)
        MODES = [
        ("Stressfrei", "1"),
        ("Gestresst", "2"),
        ("32 zus.", "3"),
        ("2x8", "4"),
        ]

        self.v = StringVar()
        self.v.set("L") # initialize
    
        for text, mode in MODES:
            b = Radiobutton(f7, text=text,variable=self.v, value=mode)
            b.pack(anchor=W)
        
        f5=LabelFrame(f2,text="Optionen")
        f5.pack(fill=BOTH,expand=1);
        
        print "Trololo"
        
        b_auf=Button(f5,text="Clusterung nach Aufenthaltswahrscheinlichkeit",command=self.showClusterProb)
        b_auf.pack(fill=BOTH,expand=1)
        
        b_state_change_rate=Button(f5,text="Clusterung nach Zustandsuebergangsrate",command=self.showClusterStaytime)
        b_state_change_rate.pack(fill=BOTH,expand=1)
        
        b_corr=Button(f5,text="Clusterung nach Korrelationskoeffizient",command=self.showClusterCorr)
        b_corr.pack(fill=BOTH,expand=1) 
        
        b_xcorr=Button(f5,text="Clusterung mit Kreuzkorrelation",command=self.showClusterXCorrAll)
        b_xcorr.pack(fill=BOTH,expand=1)
        self.init_popup(f2)
        self.list.bind("<Button-3>", self.do_popup)
        
       
    #
    def poll(self):
        now = self.list.curselection()
        if now != self.current:
            self.list_has_changed(now)
            self.current = now
        self.list.after(250,self.poll)
    def list_has_changed(selection):
        print selection
       
        
        
master=Tk();
app=App(master)
master.title("Dyadenklassifikation")
master.mainloop()
