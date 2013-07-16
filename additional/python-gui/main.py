from Tkinter import *
import pickle
import time
import tkFont 

class App:
    list;
    def init_popup(self,root):
        self.popup = Menu(root, tearoff=0)
        self.popup.add_command(label="Diagramm") # , command=next) etc...
        self.popup.add_command(label="XCorr")
        self.popup.add_separator()
        self.popup.add_command(label="Home")

    def do_popup(self,event):
        # display the popup menu 
        self.popup.tk_popup(event.x_root, event.y_root,1)
                
    def party(self,event):
            print "Hallo"
    
    def __init__(self,master):
        # Alle Dyandennr. einlesen
        
        file=open("../../Daten/zeitreihen.data");
        zeitreihen=pickle.load(file)
        #print zeitreihen

        dyade_num=len(zeitreihen)
        f=open("../../Daten/id_lst.data");
        ids=pickle.load(f)
        
        # Aufbau der GUI
        
        frame=Frame(master)
        frame.pack(fill=BOTH,expand=1)
        
        f1=Frame(frame)
        f1.pack(pady=20)
        
        
        l=Label(f1,text="Bitte waehlen Sie die auszuschliessenden Dyaden:")
        f = tkFont.Font(l,("Sans Serif",12))
        l.configure(font=f)
        l.pack()
        
        f2=Frame(frame)
        f2.pack(fill=BOTH,expand=1)
        
        f3=Frame(f2)
        f3.pack(side=LEFT,fill=BOTH)
        
        f4=Frame(f3)
        f4.pack(fill=BOTH,expand=1)
        scrollbar=Scrollbar(f4,orient=VERTICAL)
        self.list=Listbox(f4,font=("Arial", 10),yscrollcommand=scrollbar.set,selectmode=MULTIPLE,selectbackground="red",selectforeground="white")
        scrollbar.config(command=self.list.yview)
        for item in ids:
            self.list.insert(0,"Dyade "+item)
        self.list.pack(fill=Y,side=LEFT)
        scrollbar.pack(side=LEFT,fill=Y)
        
        #Entry(f2,textvariable=text).grid(row=0,column=1)
        self.current=self.list.curselection()
        self.poll()
        
        b_reset=Button(f3,text="Zuruecksetzen",command=self.list.selection_clear(FIRST,LAST))
        b_reset.pack(fill=BOTH)
        
        f5=LabelFrame(f2,text="Optionen")
        f5.pack(fill=BOTH,expand=1);
        
        print "Halo"
        
        b_auf=Button(f5,text="Clusterung nach Aufenthaltswahrscheinlichkeit")
        b_auf.pack(fill=BOTH,expand=1)
        
        b_state_change_rate=Button(f5,text="Clusterung nach Zustandsuebergangsrate")
        b_state_change_rate.pack(fill=BOTH,expand=1)
        
        b_corr=Button(f5,text="Clusterung nach Korrelationskoeffizient")
        b_corr.pack(fill=BOTH,expand=1)
        
        b_xcorr=Button(f5,text="Clusterung mit Kreuzkorrelation")
        b_xcorr.pack(fill=BOTH,expand=1)
        self.init_popup(f2)
        self.list.bind("<Button-3>", self.do_popup)
    
    
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