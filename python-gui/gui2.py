from Tkinter import *
import time
class App:
    list;
    def __init__(self,master):
        text="Hello"
        frame=Frame(master)
        frame.pack(side=LEFT,fill=Y)
        f2=Frame(master,bg="red")
        f2.pack(expand=1,fill=BOTH)
        
        f3=Frame(frame)
        f3.pack()
        f4=Frame(frame)
        f4.pack(fill=Y,expand=1)
        
        scrollbar=Scrollbar(f4,orient=VERTICAL)
        self.list=Listbox(f4,font=("Arial", 20),yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.list.yview)
        scrollbar.pack(side=RIGHT,fill=Y)
        liste=["hi","du","da","du","da","hi","du","da","du","da","hi","du","da","du","da","hi"]
        for item in liste:
            self.list.insert(0,item)
        self.list.pack(fill=BOTH,expand=1,side=LEFT)
        Label(f3,text="Choose one").pack(side=TOP,fill=X,expand=1)
        
        Button(f2,text="Hello").grid(row=0,column=1);
        Button(f2,text="Lapp3n").grid(row=1,column=2)
        Button(f2,text="Lapp3!n").grid(row=2,column=3)
        #Entry(f2,textvariable=text).grid(row=0,column=1)
        self.current=self.list.curselection()
        self.poll()
        

    def poll(self,):
        now = self.list.curselection()
        if now != self.current:
            self.list_has_changed(now)
            self.current = now
        self.list.after(250,self.poll)
    def list_has_changed(selection):
        print selection
       
        
        
master=Tk();
app=App(master)
master.mainloop()