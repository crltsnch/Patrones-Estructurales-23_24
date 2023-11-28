from compositeEstructura import *
from proxy import Proxy
from guardarArchivos import *
from registros import *

if __name__ == "__main__":

    '''Carpeta 1'''
    ruta_carpeta = Carpeta("Imagenes")
    carpeta1 = Carpeta("Carpeta1")
    carpeta2 = Carpeta("Carpeta2")
    documento1 = Documento("Confidencial.txt", "txt", 1000, sensible=True)
    documento2 = Documento("img.jpg", "image", 900)
    link1 = Link("Link to Carpeta2", tamaño=10)

    '''Carpeta 2'''
    ruta_carpeta2 = Carpeta("Videos")
    carpeta3 = Carpeta("Videos vacaciones")
    carpeta4 = Carpeta("Videos trabajo")
    documento3 = Documento("video1.mp4", "video", 1100, sensible=True)
    documento4 = Documento("video2.mp4", "video", 1200)
    link2 = Link("Link to video1.mp4", tamaño=10)

    
    #Construir la estructura del sistema
    ruta_carpeta.add(carpeta1)
    ruta_carpeta.add(link1)
    carpeta1.add(documento1)
    carpeta1.add(carpeta2)
    carpeta2.add(documento2)


    ruta_carpeta2.add(carpeta3)
    ruta_carpeta2.add(carpeta4)
    carpeta3.add(documento3)
    carpeta3.add(link2)
    carpeta4.add(documento4)


    #Mostrar la estructura del sistema
    client_code(ruta_carpeta)
    print("\n")
    #Mostrar el tamaño de la carpeta
    print(f"Tamaño de la carpeta {ruta_carpeta.nombre}: {ruta_carpeta.get_tamaño()} bytes")
    print("\n")
    client_code(ruta_carpeta2)
    print("\n")
    #Mostrar el tamaño de la carpeta
    print(f"Tamaño de la carpeta {ruta_carpeta2.nombre}: {ruta_carpeta2.get_tamaño()} bytes")

    proxy_documento1 = Proxy(documento1)
    proxy_documento2 = Proxy(documento2)
    #Intentar acceder al documento1 a través del proxy
    usuario_ingresado = input("Introduzca su nombre de usuario: ")
    proxy_documento1.acceder = logger(proxy_documento1.acceder)
    proxy_documento2.acceder = logger(proxy_documento2.acceder)
    if usuario_ingresado:
        proxy_documento1.acceder(usuario=usuario_ingresado)
        proxy_documento2.acceder(usuario=usuario_ingresado)

    #Mostrar los regristos de acceso del proxy
    proxy_documento1.mostrar_registros()

    guardar_en_json(ruta_carpeta.mostrar(), "archivo.json")
    guardar_en_json(ruta_carpeta2.mostrar(), "archivo.json")

