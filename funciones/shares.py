

def agregar_smb_conf(sharedName="", sharedDesc="", directoryPath="", readOnly=0):
    ruta_smb_conf = '/etc/samba/smb.conf'
    
    if readOnly == 0:
        readOnly = "no"
    else:
        readOnly = "yes"

    conf_nuevo = f"""
[{sharedName}]
        comment = {sharedDesc}
        path = {directoryPath}
        read only = {readOnly}
    """

    print(conf_nuevo)

    try:
        with open(ruta_smb_conf, 'a') as file:
            file.write(conf_nuevo + "\n")
        print("Se ha agregado la configuracion")
    except PermissionError:
        print(f"No existen permisos para modificar el archivo {ruta_smb_conf}")
    
def eliminar_smb_conf(seccion):
    ruta_smb_conf = "/etc/samba/smb.conf"
    
    try:
        with open(ruta_smb_conf, 'r') as file:
            lineas = file.readlines()

        nueva_lineas = []
        en_seccion = False

        for linea in lineas:
            if linea.strip().startswith('[') and linea.strip().endswith(']'):
                if linea.strip()[1:-1] == seccion:
                    
                    en_seccion = True
                else:
                    en_seccion = False
                    nueva_lineas.append(linea)
            elif not en_seccion:
                nueva_lineas.append(linea)

        with open(ruta_smb_conf, 'w') as file:
            file.writelines(nueva_lineas)
        
        print(f"Sección [{seccion}] eliminada.")
    except PermissionError:
        print(f"No tienes permisos para modificar el archivo {ruta_smb_conf}.")

def leer_smb_conf():
    ruta_smb_conf = "/etc/samba/smb.conf"
    
    try:
        with open(ruta_smb_conf, 'r') as file:
            contenido = file.read()
        print(contenido)
    except FileNotFoundError:
        print(f"No se encontró el archivo {ruta_smb_conf}.")
    except PermissionError:
        print(f"No tienes permisos para leer el archivo {ruta_smb_conf}.")

#leer_smb_conf()
#agregar_smb_conf("COMPARTIDOS", "carpeta compartida", "/home/compartido", 1)

eliminar_smb_conf("COMPARTIDOS")