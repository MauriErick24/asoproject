import tkinter as tk
from tkinter import ttk

def leer_valores(ruta_archivo):
    secciones = {}
    parametros = ["status", "read only", "path", "guest ok", "guest access", "comment"]
    
    try:
        with open(ruta_archivo, 'r') as archivo:
            nombre_seccion = None
            for linea in archivo:
                linea = linea.strip()
                if linea.startswith("[") and linea.endswith("]"):
                    nombre_seccion = linea[1:-1]
                    secciones[nombre_seccion] = {}
                elif nombre_seccion is not None:
                    partes = linea.split('=', 1)
                    if len(partes) == 2:
                        parametro = partes[0].strip()
                        valor = partes[1].strip()
                        if parametro in parametros:
                            secciones[nombre_seccion][parametro] = valor
                    else:
                        print(f"")

        return secciones
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None


class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.frameBase = tk.Frame(ventana, bg="black")
        self.frameBase.pack(side="right", expand=True, fill="both")

        self.menu_visible = False
        self.crear_menu()
        self.crear_boton_menu()

    def crear_menu(self):
        self.menu_frame = tk.Frame(self.ventana, bg="#493d3f", width=800)
        self.menu_frame.place(x=-500, y=0, relheight=1)

        btn1 = tk.Button(self.menu_frame, text="Start-Up", bg="#d8d989", fg="black", relief="raised",
                         font=("Comic Sans MS", 10), command=lambda: self.StarUp())
        btn1.pack(pady=50)

        btn2 = tk.Button(self.menu_frame, text="Shares", bg="#d8d989", fg="black", relief="raised",
                         font=("Comic Sans MS", 11), command=lambda: self.Shares())
        btn2.pack(pady=10)

        btn3 = tk.Button(self.menu_frame, text="Identity", bg="#d8d989", fg="black", relief="raised",
                         font=("Comic Sans MS", 11), command=lambda: self.Identity())
        btn3.pack(pady=50)

    def crear_boton_menu(self):
        self.menu_button = tk.Button(self.ventana, text="≡", bg="#493d3f", fg="white", command=self.toggle_menu)
        self.menu_button.place(x=0, y=0)

    def toggle_menu(self):
        if self.menu_visible:
            self.ocultar_menu()
        else:
            self.mostrar_menu()

    def mostrar_menu(self):
        x = -50
        while x < 0:
            self.menu_frame.place(x=x, y=0)
            self.menu_frame.update()
            x += 20
        self.menu_visible = True

    def ocultar_menu(self):
        x = 0
        while x > -150:
            self.menu_frame.place(x=x, y=0)
            self.menu_frame.update()
            x -= 10
        self.menu_visible = False

    def StarUp(self):
        for widget in self.frameBase.winfo_children():
            widget.destroy()

        frameStarUp = tk.Frame(self.frameBase, bg="#bdb495")
        frameStarUp.pack(expand=True, fill="both")

        lab1 = tk.Label(frameStarUp, bg="#f8f2ce", fg="black", text="Configuracion de servicios", font=("Courier New", 25))
        lab1.place(relx=0.30, rely=0.1)

        lab2 = tk.Label(frameStarUp, bg="#f8f2ce", fg="black", text="Despues de escribir la configuracion", font=("Courier New", 16))
        lab2.place(relx=0.1, rely=0.3)

        lab3 = tk.Label(frameStarUp, bg="#f8f2ce", fg="black", text="Despues de reiniciar", font=("Courier New", 16))
        lab3.place(relx=0.1, rely=0.5)

        combo1 = ttk.Combobox(frameStarUp, 
                              values=["Recargar", "No Recargar"],
                              justify="center",
                              font=("Comic Sans MS", 12))
        combo1.set("Recargar")
        combo1.place(relx=0.1, rely=0.4)

        combo2 = ttk.Combobox(frameStarUp,
                              values=["No iniciar", "Iniciar"],
                              justify="center",
                              font=("Comic Sans MS", 12),
                              state="readonly")
        combo2.set("No iniciar")
        combo2.place(relx=0.1, rely=0.6)
        

    def Shares(self):
        for widget in self.frameBase.winfo_children():
            widget.destroy()

        frameShares = tk.Frame(self.frameBase, bg="#bdb495")
        frameShares.pack(expand=True, fill="both")

        # Crear el widget Treeview
        columnas = ["Name", "status", "read only", "path", "guest ok", "guest access", "comment"]
        tv = ttk.Treeview(frameShares, columns=columnas, show='headings')

        # Definir los encabezados de las columnas
        for col in columnas:
            tv.heading(col, text=col, anchor=tk.CENTER)

        # Definir el ancho de las columnas y ajustar el alto de las filas
        tv.column("Name", width=90, anchor=tk.CENTER)
        tv.column("status", width=70, anchor=tk.CENTER)
        tv.column("read only", width=100, anchor=tk.CENTER)
        tv.column("path", width=150, anchor=tk.CENTER)
        tv.column("guest ok", width=100, anchor=tk.CENTER)
        tv.column("guest access", width=10, anchor=tk.CENTER)
        tv.column("comment", width=150, anchor=tk.CENTER)
        tv.configure(height=4)  # Número de filas que deseas mostrar

        # Posicionar la tabla dentro del frameShares con margen izquierdo y derecho
        tv.place(relx=0, rely=0, relwidth=0.8, relheight=0.2)

        # Leer valores del archivo y agregarlos a la tabla
        ruta_archivo = 'D:\\Archivos Personales\\Programacion\\Ejercicios python\\ejem.txt'
        secciones = leer_valores(ruta_archivo)
        if secciones:
            for nombre_seccion, valores in secciones.items():
                tv.insert('', 'end', values=(
                    nombre_seccion,
                    valores.get("status", ""),
                    valores.get("read only", ""),
                    valores.get("path", ""),
                    valores.get("guest ok", ""),
                    valores.get("guest access", ""),
                    valores.get("comment", "")
                ))

        # Crear el Scrollbar
        scrollbar = ttk.Scrollbar(frameShares, orient="vertical", command=tv.yview)
        tv.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        



    def Identity(self):
        for widget in self.frameBase.winfo_children():
            widget.destroy()

        frameIdentity = tk.Frame(self.frameBase, bg="yellow")
        frameIdentity.pack(expand=True, fill="both")

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.config(bg="black")
    ventana.title("ADMINISTRADOR SAMBA")
    app = Aplicacion(ventana)
    ventana.update_idletasks()
    ventana.geometry(f"{ventana.winfo_width()}x{ventana.winfo_height()}+{ventana.winfo_x()}+{ventana.winfo_y()}")
    ventana.mainloop()
