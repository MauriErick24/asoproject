import PIL.Image
from PIL import Image,ImageTk
from tkinter import *
from tkinter import ttk
from Credencial import *
from Aplicacion import *

class Login:
  def __init__(self):
  
   self.raiz = Tk()
   self.raiz.geometry("370x250")
   self.raiz.config(bg="black")
   self.raiz.title("Inicio Secion")
   self.raiz.config(background="black")
   self.raiz.config(relief="raised")

   frameimage = Frame(self.raiz,bg="#333333" ,width=150)
   frameimage.pack(side="left",fill="y")

   label_imagen = Label(frameimage)
   label_imagen.place(relx=0.1,rely=0.6)

   imagen =  PIL.Image.open('Interfaz/suse.png')
   imagen.thumbnail((100,100))
   imagen = ImageTk.PhotoImage(imagen)
   label_imagen.config(image=imagen)
   label_imagen.image = imagen

   label_imagen2 = Label(frameimage)
   label_imagen2.place(relx=0.1,rely=0.1)

   imagena =  PIL.Image.open('Interfaz/maba.png')
   imagena.thumbnail((100,100))
   imagena = ImageTk.PhotoImage(imagena)
   label_imagen2.config(image=imagena)
   label_imagen2.image = imagena
   
  
   # Crea un widget Label y asigna la imagen
   
   
   lbl1 = tk.Label(self.raiz, text="Autenticación de SuperUsuario", bg="#333333", fg="white")
   lbl1.pack(pady=10)

   lbl2 = tk.Label(self.raiz, text="Ingrese su contraseña", bg="#333333", fg="white")
   lbl2.pack(pady=20)
   self.text1 = ttk.Entry(self.raiz)
   self.text1.pack(pady=15)

   btn = Button(self.raiz, text="Ingresar", command=self.verificar,bg="#333333", fg="white")
   btn.pack(pady=15)

   self.raiz.mainloop()

  def verificar(self):
      p = Credecial()
      res = p.leer(self.text1.get())
      if res:
       self.raiz.destroy()
       app = Aplicacion()
      
      else:
         mensage = tk.Message(self.raiz,text="Intruso")
         self.raiz.destroy()
