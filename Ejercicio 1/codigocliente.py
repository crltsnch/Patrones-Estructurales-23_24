from componente import Menu

def client_code(mensaje, opciones) -> None: 
    """
    El código del cliente funciona con todos los componentes a través de la interfaz base. Vamos a pedirle al cliente si quiere crear su menu o elegir uno ya hecho.
    """
    while True:
        try:
            eleccion = int(input(mensaje))
            if eleccion in opciones:
                return eleccion
            else:
                print("Opción no disponible")

        except ValueError:
            print("Opción no disponible")
    