from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import pandas as pd

data = pd.read_csv('/Users/carlotasanchezgonzalez/Documents/class/Patrones-Estructurales-23_24/Ejercicio 1/data/data_final.csv', sep=';', encoding='ISO-8859-1')

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

class CompositeComboPareja(Menu):
    def __init__(self, nombre):
        self.nombre = nombre
        self.combo1 = None
        self.combo2 = None
    
    def personalizar(self, combo1: Menu, combo2: Menu):
        self.combo1 = combo1
        self.combo2 = combo2

    def mostrar(self) -> str:
        print(f"Combo Pareja: {self.nombre}")
        self.combo1.mostrar()
        self.combo2.mostrar()
        print(f"Precio total del Combo: {self.precio_total()}")

    def precio_total(self) -> float:
        precio_combo1 = self.combo1.precio_total()
        precio_combo2 = self.combo2.precio_total()
        return precio_combo1 + precio_combo2


def client_code(mensaje, opciones) -> None:   #menu simple
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
        pizzas_disponibles = data[["pizza_name", "total_price"]].drop_duplicates()

        instancias_pizzas = [Pizza(nombre, precio) for nombre, precio in pizzas_disponibles.values]

        # Permitir al cliente elegir su menu dandole a elegir entre los entrantes y pizzas disponibles mediante un numero
        print("\nEntrantes disponibles:")
        for i, entrante in enumerate(instancias_entrantes, start=1):
            print(f"{i}. {entrante.nombre} - Precio: {entrante.precio}")

        eleccion_entrante = client_code("Elige un entrante (número): ", list(range(1, len(instancias_entrantes) + 1)))
        entrante_personalizado = instancias_entrantes[eleccion_entrante - 1]

        print("\nPizzas disponibles:")
        for i, pizza in enumerate(instancias_pizzas, start=1):
            print(f"{i}. {pizza.nombre} - Precio: {pizza.precio}")

        eleccion_pizza = client_code("Elige una pizza (número): ", list(range(1, len(instancias_pizzas) + 1)))
        pizza_personalizada = instancias_pizzas[eleccion_pizza - 1]

        # Crear menú personalizado
        nombre_combo = input("Elige un nombre para tu combo: ")
        menu_personalizado = CompositeCombo(nombre_combo)
        menu_personalizado.add(entrante_personalizado)
        menu_personalizado.add(pizza_personalizada)

        print("\nMenú Personalizado:")
        menu_personalizado.mostrar()

    elif eleccion == 2:
        print("¡Vamos a elegir un menu ya hecho!")
        
        '''----------Combo Predefinido 1----------'''

        #Creamos las intancias de entrantes y pizzas para añadir a nuestro combo prefenido
        entrante11 = Entrante("salsa cesar", 3.5)
        entrante12 = Entrante("nachos", 6.5)
        pizza11 = Pizza("The Mediterranean Pizza", data[data["pizza_name"] == "The Mediterranean Pizza"]["total_price"].unique()[0])
        pizza12 = Pizza("The Brie Carre Pizza", data[data["pizza_name"] == "The Brie Carre Pizza"]["total_price"].unique()[0])

        #Creamos el combo
        combo1 = CompositeCombo("Combo Pareja")
        combo1.add(entrante11)
        combo1.add(pizza11)
        combo1.add(entrante12)
        combo1.add(pizza12)

        print("\nCombos disponibles:")
        print("1. Combo Fiesta")
        combo1.mostrar()

        descuento = 0.2
        precio_descuento1 = combo1.precio_total() * (1 - descuento)
        print("\n¡Oferta especial! Al elegir este combo obtienes un 20% de descuento:")
        print(f"1. Combo Fiesta precio final con descuento: {round(precio_descuento1, 2)}")


