# Patrones-Estructurales-23_24

El link a mi repositorio es: [GitHub](https://github.com/crltsnch/Patrones-Estructurales-23_24.git)

## Ejercicio 1: Expansión del Sistema Integral de Pizzería "Delizioso" con Menús Personalizados y Almacenamiento en CSV utilizando los Patrones Builder y Composite

Buscamos expandir la oferta permitiendo a los clientes crear menús personalizados que incluyan entradas, bebidas, pizzas y postres. Los menús pueden ser simples o compuestos, con precios calculados según la suma de los elementos y descuentos aplicados. Utilizamos el patrón Composite para modelar la relación entre elementos y menús. Usamos CSV para almacenar y recuperar información de menús, reconstruyendo la estructura con eficiencia en tiempo de ejecución. Hemos implementado de forma modular, orientada a objetos y cumpliendo las restricciones especificadas.

La carpeta pizzas contiene la creacion de pizzas con patrón builder realizada anteriormente. Nuestro plantUML para la creación de menús es:

![menus](https://github.com/crltsnch/Patrones-Estructurales-23_24/assets/91721777/da6512ad-090a-40a8-bf84-0d8d9b897d7a)


### componente.py
La interfaz con las funciones que vamos a utilizar.
```
from __future__ import annotations
from abc import ABC, abstractmethod

class Menu(ABC):
    '''La clase Componente base declara operaciones comunes tanto para los objetos
    simples como para los compuestos de una composición.'''
    
    def add(self, component: Menu) -> None:
        pass

    def remove(self, component: Menu) -> None:
        pass
    
    @abstractmethod
    def mostrar(self) -> str:
        pass
```

### hojas.py

```
from __future__ import annotations
from componente import Menu



class Entrante(Menu):
    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.

    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-components.
    """

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self) -> str:
        print(f"Entrante: {self.nombre} , Precio: {self.precio}")


class Pizza(Menu):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def mostrar(self) -> str:
        print(f"Pizza: {self.nombre} , Precio: {self.precio}")


class Bebida(Menu):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def mostrar(self) -> str:
        print(f"Bebida: {self.nombre} , Precio: {self.precio}")
    
    
class Postre(Menu):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def mostrar(self) -> str:
        print(f"Postre: {self.nombre} , Precio: {self.precio}")

```

### composite.py
Aqui se crean los menús, combos simples y combos compuestos.
```
from __future__ import annotations
from componente import Menu


'''-------------COMBO------------'''

class CompositeCombo(Menu):
    """
    The Composite class represents the complex components that may have
    children. Usually, the Composite objects delegate the actual work to their
    children and then "sum-up" the result.
    """

    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    """
    A composite object can add or remove other components (both simple or
    complex) to or from its child list.
    """

    def add(self, componente: Menu) -> None:
        self.componentes.append(componente)

    def remove(self, componente: Menu) -> None:
        self.componentes.remove(componente)
    
    def mostrar(self) -> str:
        print(f"Combo: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar()
        
        print(f"Precio total del Combo: {self.precio_total()}")

    def precio_total(self) -> float:
        """
        The Composite executes its primary logic in a particular way. It
        traverses recursively through all its children, collecting and summing
        their results. Since the composite's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result.
        """

        total_price = 0
        for componente in self.componentes:
            total_price += componente.precio
        return total_price
    

'''-------------COMBO PAREJA------------'''

class CompositeComboCompuesto(Menu):
    def __init__(self, nombre):
        self.nombre = nombre
        self.combo1 = None
        self.combo2 = None
    
    def personalizar(self, combo1: Menu, combo2: Menu):
        self.combo1 = combo1
        self.combo2 = combo2

    def mostrar(self) -> str:
        print(f"Combo Compuesto: {self.nombre}")
        self.combo1.mostrar()
        print("\n")
        self.combo2.mostrar()
        print(f"Precio total del Combo: {self.precio_total()}")

    def precio_total(self) -> float:
        precio_combo1 = self.combo1.precio_total()
        precio_combo2 = self.combo2.precio_total()
        return precio_combo1 + precio_combo2
```

### codigocliente.py
```
from componente import Menu

#Cliente
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
```

### run.py
Aqui hemos creado menús y combos.
```
from __future__ import annotations
import pandas as pd
from codigocliente import client_code
from hojas import Entrante, Pizza, Bebida, Postre
from composite import CompositeCombo, CompositeComboCompuesto
from guardarmenus import guardar_menu_personalizado

data = pd.read_csv('/Users/carlotasanchezgonzalez/Documents/class/Patrones-Estructurales-23_24/Ejercicio 1/pizzas/data/data_final.csv', sep=';', encoding='ISO-8859-1')

if __name__ == "__main__":
    """
    This way the client code can support the simple leaf components...
    """
    print("Bienvenido a la pizzeria")
    print("¿Quieres crear tu propio menu o elegir uno ya hecho?")
    
    opciones = [1, 2]
    mensaje = "1. Crear menu \n2. Elegir menu ya hecho \nElige una opción: "
    eleccion = client_code(mensaje, opciones)



    if eleccion == 1:
        print("¡Vamos a crear tu menu!")

        # Generar instancias de Entrante con todos los entrantes y precios disponibles
        entrantes_disponibles = [
             ("salsa cesar", 3.5),
            ("alitas de pollo a la parrilla", 5.5),
            ("nachos", 6.5),
            ("mini calzones", 4.5),
            ("rollitos de primavera caprese", 7.5)
        ]
        instancias_entrantes = [Entrante(nombre, precio) for nombre, precio in entrantes_disponibles]

        # Generar instancias de Pizza con todos los nombres y precios disponibles
        pizzas_disponibles = data.groupby('pizza_name')['total_price'].first().reset_index()
        instancias_pizzas = [Pizza(nombre, precio) for nombre, precio in pizzas_disponibles.values]

        #Generar instancias de Bebida con todos los nombres y precios disponibles  
        bebidas_disponibles = [
            ("Garnacha", 2.5),
            ("Chardonnay", 3.5),
            ("Viura", 3.5),
            ("Albariño", 4.5),
            ("Cerveza de trigo", 3),
            ("Cerveza rubia", 3.5),
            ("Cerveza tostada", 3.5),
            ("Cerveza con limón", 3),
            ("Limonada Casera", 2.5),
            ("Agua", 1.5),
            ("Agua con gas", 1.7),
            ("Cola", 2),
            ("Leche", 2)
        ]
        instancias_bebidas = [Bebida(nombre, precio) for nombre, precio in bebidas_disponibles]


        #Generar instacias de Postre con todos los nombres y precios disponibles
        postres_disponibles = [
            ("Tarta de queso", 5.5),
            ("Mousse de chocolate", 4.5),
            ("Tarta de zanahoria", 4.5),
            ("Helado variado", 3.5),
            ("Tiramisu", 5.5)
        ]


        # Permitir al cliente elegir su menu dandole a elegir entre los entrantes mediante un numero
        print("\nEntrantes disponibles:")
        for i, entrante in enumerate(instancias_entrantes, start=1):
            print(f"{i}. {entrante.nombre} - Precio: {entrante.precio}")

        eleccion_entrante = client_code("Elige un entrante (número): ", list(range(1, len(instancias_entrantes) + 1)))
        entrante_personalizado = instancias_entrantes[eleccion_entrante - 1]

        # Permitir al cliente elegir su menu dandole a elegir entre las pizzas disponibles mediante un numero
        print("\nPizzas disponibles:")
        for i, pizza in enumerate(instancias_pizzas, start=1):
            print(f"{i}. {pizza.nombre} - Precio: {pizza.precio}")

        eleccion_pizza = client_code("Elige una pizza (número): ", list(range(1, len(instancias_pizzas) + 1)))
        pizza_personalizada = instancias_pizzas[eleccion_pizza - 1]

        # Permitir al cliente elegir su menu dandole a elegir entre las bebidas disponibles mediante un numero
        print("\nBebidas disponibles:")
        for i, bebida in enumerate(instancias_bebidas, start=1):
            print(f"{i}. {bebida.nombre} - Precio: {bebida.precio}")
        
        eleccion_bebida = client_code("Elige una bebida (número): ", list(range(1, len(instancias_bebidas) + 1)))
        bebida_personalizada = instancias_bebidas[eleccion_bebida - 1]

        # Permitir al cliente elegir su menu dandole a elegir entre los postres disponibles mediante un numero
        print("\nPostres disponibles:")
        for i, (nombre_postre, precio_postre) in enumerate(postres_disponibles, start=1):
            print(f"{i}. {nombre_postre} - Precio: {precio_postre}")

        eleccion_postre = client_code("Elige un postre (número): ", list(range(1, len(postres_disponibles) + 1)))
        nombre_postre, precio_postre = postres_disponibles[eleccion_postre - 1]
        postre_personalizado = Postre(nombre_postre, precio_postre)

        # Crear menú personalizado
        nombre_combo = input("Elige un nombre para tu combo: ")
        menu_personalizado = CompositeCombo(nombre_combo)
        menu_personalizado.add(entrante_personalizado)
        menu_personalizado.add(pizza_personalizada)
        menu_personalizado.add(bebida_personalizada)
        menu_personalizado.add(postre_personalizado)

        print("\nMenú Personalizado:")
        menu_personalizado.mostrar()
        

        # Guardar menú personalizado
        guardar_menu_personalizado(menu_personalizado)



    elif eleccion == 2:
        print("¡Vamos a elegir un menu de nuestras creaciones!\n")
        
        '''----------Combo Predefinido 1----------'''
        #Creamos las intancias de entrantes y pizzas para añadir a nuestro combo individual prefenido
        entrante1 = Entrante("salsa cesar", 3.5)
        pizza1 = Pizza("The Mediterranean Pizza", data[data["pizza_name"] == "The Mediterranean Pizza"]["total_price"].unique()[0])
        bebida1 = Bebida("Cola", 2.5)
        postre1 = Postre("Tarta de queso", 5.5)


        #Creamos el combo
        combo1 = CompositeCombo("Combo Individual")
        combo1.add(entrante1)
        combo1.add(pizza1)
        combo1.add(bebida1)
        combo1.add(postre1)

        print("Combo Individual")
        combo1.mostrar()

        descuento = 0.2
        precio_descuento1 = combo1.precio_total() * (1 - descuento)
        print("\n¡Oferta especial! Al elegir este combo obtienes un 20% de descuento:")
        print(f"Combo Individual precio final con descuento: {round(precio_descuento1, 2)}\n")


        '''----------Combo Predefinido 2----------'''
        pizza2 = Pizza("The Prosciutto and Arugula Pizza", data[data["pizza_name"] == "The Prosciutto and Arugula Pizza"]["total_price"].unique()[0])
        postre2 = Postre("Tiramisu", 5.5)

        combo2 = CompositeCombo("Combo Sencillo")
        combo2.add(pizza2)
        combo2.add(postre2)

        print("Combo Sencillo")
        combo2.mostrar()

        descuento = 0.1
        print("\n¡Oferta especial! Al elegir este combo obtienes un 10% de descuento:")
        precio_descuento2 = combo2.precio_total() * (1 - descuento)
        print(f"Combo Sencillo precio final con descuento: {round(precio_descuento2, 2)}\n")


        '''----------Combo Predefinido 3----------'''
        entrante3 = Entrante("nachos", 5.5)
        pizza3 = Pizza("The Thai Chicken Pizza", data[data["pizza_name"] == "The Thai Chicken Pizza"]["total_price"].unique()[0])
        bebida3 = Bebida("Albariño", 4.5)
        postre3 = Postre("Mousse de chocolate", 4.5)

        combo3 = CompositeCombo("Combo Deluxe")
        combo3.add(entrante3)
        combo3.add(pizza3)
        combo3.add(bebida3)
        combo3.add(postre3)

        print("Combo Deluxe")
        combo3.mostrar()


        descuento = 0.2
        precio_descuento3 = combo3.precio_total() * (1 - descuento)
        print("\n¡Oferta especial! Al elegir este combo obtienes un 20% de descuento:")
        print(f"Combo Individual precio final con descuento: {round(precio_descuento3, 2)}\n")




        '''----------Combo Compuesto 1----------'''
        # Creamos un combo compuesto con el combo1 y combo2 con descuento
        combo_compuesto1 = CompositeComboCompuesto("Combo Pareja")
        combo_compuesto1.personalizar(combo1, combo2)
        combo_compuesto1.mostrar()

        descuento = 0.3
        precio_descuento2 = combo_compuesto1.precio_total() * (1 - descuento)
        print("\n¡Oferta especial! Al elegir este combo obtienes un 30% de descuento:")
        print(f"Combo Pareja precio final con descuento: {round(precio_descuento2, 2)}\n")

        '''----------Combo Compuesto 2----------'''
        # Creamos un combo compuesto con el combo1 y combo3 con descuento
        combo_compuesto2 = CompositeComboCompuesto("Combo Familiar")
        combo_compuesto2.personalizar(combo1, combo3)
        combo_compuesto2.mostrar()

        descuento = 0.1
        precio_descuento2 = combo_compuesto1.precio_total() * (1 - descuento)
        print("\n¡Oferta especial! Al elegir este combo obtienes un 10% de descuento y gana 2 entradas para el cine:")
        print(f"Combo Pareja precio final con descuento: {round(precio_descuento2, 2)}\n")





        '''----------Selección de Combo----------'''
        while True:
            print("1. Combo Individual")
            print("2. Combo Sencillo")
            print("3. Combo Deluxe")
            print("4. Combo Pareja")
            print("5. Combo Familiar")
            combo_elegido = int(input("¿Qué combo deseas? (número) o deseas salir (6): "))
            combos = [1, 2, 3, 4, 5, 6]

            if combo_elegido not in combos:
                print("Opción no disponible")
                continue
            
            if combo_elegido == 6:
                break

            
            print("¡Gracias por elegirnos!")
            print("Tu pedido está en marcha...")
            print("¡Buen provecho!")
            break
                

    else:
        print("Opción no válida. Vuelve a intentarlo.")
```

### guardarmenus.py
Mi siguiente paso ha sido guardar los menús creados en un csv.
```
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
```
Se nos guarda de esta forma:
id;nombre;entrante;pizza;bebida;postre;precio_total
NS8TML;hola;nachos;The Brie Carre Pizza;Viura;Tarta de zanahoria;38.15
MM4GZ2;c;alitas de pollo a la parrilla;The Brie Carre Pizza;Albariño;Tarta de zanahoria;38.15
QQCOHM;w;mini calzones;The Chicken Alfredo Pizza;Chardonnay;Tiramisu;26.25


## leermenus.py
Después he implementado funciones para leer esos menús guardados y reconstruirlos.
```
import csv

def leer_pizzas_desde_csv(archivo_csv):
    menus = []
    with open(archivo_csv, 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            menus.append(row)
    return menus

def reconstruir_menu(datos):
    menu = f"ID: {datos['id']}\n"
    menu += f"Nombre: {datos['nombre']}\n"
    menu += f"Entrante: {datos['entrante']}\n"
    menu += f"Pizza: {datos['pizza']}\n"
    menu += f"Bebida: {datos['bebida']}\n"
    menu += f"Postre: {datos['postre']}\n"
    return menu

if __name__ == "__main__":
    archivo_csv = "Ejercicio 1/menus.csv"
    menus = leer_pizzas_desde_csv(archivo_csv)
    for menu in menus:
        print(reconstruir_menu(menu))
```

### test.py
Por último aqui hemos pasado pruebas.
```
import unittest
from unittest.mock import patch
from codigocliente import client_code
from hojas import Entrante, Pizza, Bebida, Postre
from composite import CompositeCombo, CompositeComboCompuesto

'''Pruebas unitarias que cubran casos básicos.
Cobertura de casos de borde y validación de correcta funcionalidad en diferentes escenarios'''

class TestMenus(unittest.TestCase):
    def test_entrante(self):
        entrante = Entrante("salsa cesar", 3.5)
        self.assertEqual(entrante.mostrar(), "Entrante: salsa cesar , Precio: 3.5")
    
    def test_pizza(self):
        pizza = Pizza("The Mediterranean Pizza", 12.5)
        self.assertEqual(pizza.mostrar(), "Pizza: The Mediterranean Pizza , Precio: 12.5")
    
    def test_bebida(self):
        bebida = Bebida("Cola", 2.5)
        self.assertEqual(bebida.mostrar(), "Bebida: Cola , Precio: 2.5")
    
    def test_postre(self):
        postre = Postre("Tarta de queso", 5.5)
        self.assertEqual(postre.mostrar(), "Postre: Tarta de queso , Precio: 5.5")
    
    def test_composite_combo(self):
        combo = CompositeCombo("Combo 1")
        entrante = Entrante("salsa cesar", 3.5)
        pizza = Pizza("The Mediterranean Pizza", 12.5)
        bebida = Bebida("Cola", 2.5)
        postre = Postre("Tarta de queso", 4.5)

        combo.add(entrante)
        combo.add(pizza)
        combo.add(bebida)
        combo.add(postre)

        with patch("sys.stdout") as mock_stdout:
            combo.mostrar()
            expected_output = "Combo: Combo 1\nEntrante: salsa cesar , Precio: 3.5\nPizza: The Mediterranean Pizza , Precio: 12.5\nBebida: Cola , Precio: 2.5\nPostre: Tarta de queso , Precio: 4.5\n"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
        

    def test_composite_combo_compuesto(self):
        combo_compuesto = CompositeComboCompuesto("Combo Compuesto")
        combo1 = CompositeCombo("Combo 1")
        combo2 = CompositeCombo("Combo 2")

        entrante = Entrante("salsa cesar", 3.5)
        pizza = Pizza("The Mediterranean Pizza", 12.5)
        bebida = Bebida("Cola", 2.5)
        postre = Postre("Tarta de queso", 4.5)

        combo1.add(entrante)
        combo1.add(pizza)
        combo1.add(bebida)
        combo1.add(postre)

        combo2.add(pizza)
        combo2.add(postre)

        combo_compuesto.personalizar(combo1, combo2)

        with patch("sys.stdout") as mock_stdout:
            combo_compuesto.mostrar()
            expected_output = "Combo Compuesto: combo_compuesto\nCombo: Combo1\nEntrante: salsa cesar , Precio: 3.5\nPizza: The Mediterranean Pizza , Precio: 12.5\nBebida: Cola , Precio: 2.5\nPostre: Tarta de queso , Precio: 4.5\nCombo: Combo 2\nPizza: The Mediterranean Pizza , Precio: 12.5\nPostre: Tarta de queso , Precio: 4.5\nPrecio total del Combo: 40.0\n\nCombo: Combo2\nPizza: The Mediterranean Pizza , Precio: 12.5\nPostre: Tarta de queso , Precio: 4.5\nPrecio total del Combo: 17.0\n\nPrecio total del Combo Compuesto: 57.0\n"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    
    def test_client_code(self):
        #Prueba la función de entrada del usuario con entrada válida
        with patch("builtins.input", return_value="1"):
            self.assertEqual(client_code("Elige un postre (número): ", list(range(1, 3))), 1)
        
        #Prueba la función de entrada del usuario con entrada inválida
        with patch("builtins.input", side_effect=["invalid", "3"]):
            self.assertEqual(client_code("Elige un postre (número): ", list(range(1, 3))), 3)


if __name__ == "__main__":
    unittest.main()
```

