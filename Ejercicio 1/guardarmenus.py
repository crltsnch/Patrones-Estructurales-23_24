import csv
import os
import random
import string
from hojas import Entrante, Pizza, Bebida, Postre

def guardar_menu_personalizado(menu_personalizado):
    carpeta_ejercicio2 = 'Ejercicio 1'
    ruta_archivo = os.path.join(carpeta_ejercicio2, 'menus.csv')

    with open(ruta_archivo, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "nombre", "entrante", "pizza", "bebida", "postre", "precio_total"], delimiter=';')

        if file.tell() == 0:
            writer.writeheader()

        # Generar ID aleatorio
        menu_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        # Obtener elementos internos del CompositeCombo
        entrante = next((c for c in menu_personalizado.componentes if isinstance(c, Entrante)), None)
        pizza = next((c for c in menu_personalizado.componentes if isinstance(c, Pizza)), None)
        bebida = next((c for c in menu_personalizado.componentes if isinstance(c, Bebida)), None)
        postre = next((c for c in menu_personalizado.componentes if isinstance(c, Postre)), None)

        # Calcular precio total del menú
        precio_total = menu_personalizado.precio_total()

        datos = {
            "id": menu_id,
            "nombre": menu_personalizado.nombre,
            "entrante": entrante.nombre if entrante else "",
            "pizza": pizza.nombre if pizza else "",
            "bebida": bebida.nombre if bebida else "",
            "postre": postre.nombre if postre else "",
            "precio_total": str(precio_total)  # Convertir a cadena
        }

        writer.writerow(datos)

    print("\nMenu guardado con éxito")


