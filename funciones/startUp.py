import os
import sys

#* reinicar samba
def reiniciarSamba():
    os.system("sudo service smb restart")

#* modo administrador
def adminMode():
    if os.geteuid() != 0:
        print("Se necesita privilegios root")
        try:
            os.execvp('sudo', ['sudo', 'python3', sys.argv[0]])
        except Exception as e:
            print('Error al obtener privilegios:', e)
            sys.exit(1)

#* Iniciar samba al arrancar sistema
def agregar_comando_inicio_samba(usuario):
    comando = f"echo 'sudo service smb restart' >> /home/{usuario}/.bashrc"
    os.system(comando)

#! linea de ejecucion
usuario = "nombre_de_usuario"
agregar_comando_inicio_samba(usuario)

#* no iniciar samba al arrancar sistema
def eliminar_comando_inicio_samba(usuario):
    archivo_bashrc = f"/home/{usuario}/.bashrc"
    with open(archivo_bashrc, 'r') as file:
        lineas = file.readlines()

    lineas_filtradas = [linea for linea in lineas if 'sudo service smb restart' not in linea]

    with open(archivo_bashrc, 'w') as file:
        file.writelines(lineas_filtradas)

#! linea de ejecucion
usuario = "nombre_de_usuario"
eliminar_comando_inicio_samba(usuario)


adminMode()
reiniciarSamba()
