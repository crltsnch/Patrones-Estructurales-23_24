from compositeEstructura import *
from proxy import Proxy

if __name__ == "__main__":
    ruta_carpeta = Carpeta("Ruta")
    carpeta1 = Carpeta("Carpeta1")
    carpeta2 = Carpeta("Carpeta2")
    documento1 = Documento("Confidencial.txt", "txt", 1100, sensible=True)
    documento2 = Documento("img.jpg", "image", 1200)
    link1 = Link("Link to Carpeta2", tamaño_simbolico=10)

    proxy_documento1 = Proxy(documento1)
    
    #Construir la estructura del sistema
    ruta_carpeta.add(carpeta1)
    ruta_carpeta.add(link1)
    carpeta1.add(documento1)
    carpeta1.add(carpeta2)
    carpeta2.add(documento2)

    #Mostrar la estructura del sistema
    client_code(ruta_carpeta)
    print("\n")

    #Mostrar el tamaño de la carpeta
    print(f"Tamaño de la carpeta {ruta_carpeta.nombre}: {ruta_carpeta.get_tamaño()} bytes")

    #Intentar acceder al documento1 a través del proxy
    proxy_documento1.acceder(usuario=input("Introduzca su nombre de usuario: "))

    #Mostrar los regristos de acceso del proxy
    proxy_documento1.mostrar_registros()