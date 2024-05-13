import tkinter as tk
from tkinter import *
from tkinter import ttk

class Aplicacion:
  def __init__(self,ventana):  
  
   frameBase = tk.Frame(ventana,bg ="white",height=410,width=440)
   frameBase.place(relx=0.3,rely=0.05)
    
   frameBase2 = tk.Frame(ventana,bg ="#033649",height=410,width=150)
   frameBase2.place(relx=0.01,rely=0.05)

   btn1 = tk.Button(frameBase2,text="Start-Up",bg ="#036564",fg ="white",relief="groove",
                         width=10 ,height=3,command=lambda: StarUp(frameBase))
   btn1.place(relx=0.1,rely=0.2)
   
   btn2 = tk.Button(frameBase2,text="Shares",bg ="#036564",fg ="white",relief="groove",width=10 ,
                                   height=3, command=lambda: Shares(frameBase))
   btn2.place(relx=0.1,rely=0.4)
    
   btn3 = tk.Button(frameBase2,text="Identity",bg ="#036564",fg ="white",relief="groove",
                       width=10 ,height=3,command=lambda: Identity(frameBase))
   btn3.place(relx=0.1,rely=0.6)
   

def StarUp(frameBase):
    frameStarUp = tk.Frame(frameBase,bg="#CDB380",height=410,width=440)
    frameStarUp.place(relx=0,rely=0)

    lab1 = Label(frameStarUp,text="Configuracion de servicios")
    lab1.place(relx=0.35,rely=0.1)

    lab2 = Label(frameStarUp,text="Despues de escribir la configuracion")
    lab2.place(relx=0.1,rely=0.3)

    lab3 = Label(frameStarUp,text="Despues de reiniciar")
    lab3.place(relx=0.1,rely=0.5)
   
    opcion_elegida= tk.StringVar()
    combo1 = ttk.Combobox(frameStarUp,
        values=["recargar","no recargar"],
        state="readonly",
       # textvariable=opcion_elegida,
        justify="center")
    combo1.set("recargar")
    #opcion_elegida=combo1.get()
    combo1.place(relx=0.1,rely=0.4)
    #print(opcion_elegida)

    combo2 = ttk.Combobox(frameStarUp,
                          values=["no iniciar","iniciar"],
                          justify="center",
                          state="readonly")
    combo2.set("no iniciar") ##Debemos leer el archivo de configuracion
    combo2.place(relx=0.1,rely=0.6)
    

def Shares(frameBase):
   frameShares = tk.Frame(frameBase,bg="blue",height=410,width=440)
   frameShares.place(relx= 0,rely= 0)

def Identity(frameBase):
   frameIdentity =tk.Frame(frameBase,bg="yellow",height=410,width=440)
   frameIdentity.place(relx= 0,rely= 0)
   
if __name__  ==  "__main__":
   ventana  = tk.Tk()
   ventana.geometry("650x450")
   ventana.config(bg="black")
   ventana.title("Yast grupo")
   app = Aplicacion(ventana)
   ventana.mainloop()