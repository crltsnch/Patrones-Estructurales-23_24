from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import pandas as pd

data = pd.read_csv('/Users/carlotasanchezgonzalez/Documents/class/Patrones-Estructurales-23_24/Ejercicio 1/data/data_final.csv', sep=';', encoding='ISO-8859-1')

class Menu(ABC):
    '''La clase Componente base declara operaciones comunes tanto para los objetos
    simples como para los compuestos de una composición.'''
    
    @property
    def parent(self) -> Menu:
        return self._parent

    @parent.setter
    def parent(self, parent: Menu):
        self._parent = parent

    def add(self, component: Menu) -> None:
        pass

    def remove(self, component: Menu) -> None:
        pass

    def is_composite(self) -> bool:
        """
        You can provide a method that lets the client code figure out whether a
        component can bear children.
        """
        return False
    
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

    '''def nombre(self) -> str:
        entrantes = ["salsa cesar", "alitas de pollo a la parrilla", "nachos", "mini calzones", "rollitos de primavera caprese"]
        while True:
            self.nombre_elegido = input(f"Elige un entrante de {entrantes}: ")
            if self.nombre_elegido in entrantes:
                return self.nombre_elegido
            else:
                print("Entrante no disponible")
                return self.nombre()
    
    def precio(self) -> float:
        precios = [3.5, 5.5, 6.5, 4.5, 7.5]
        entrantes = ["salsa cesar", "alitas de pollo a la parrilla", "nachos", "mini calzones", "rollitos de primavera caprese"]
        index = entrantes.index(self.nombre_elegido)
        return precios[index]'''

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self) -> str:
        print(f"Entrante: {self.nombre} \nPrecio: {self.precio}")

class Pizza(Menu):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def mostrar(self) -> str:
        print(f"Pizza: {self.nombre} \nPrecio: {self.precio}")


''' def nombre(self) -> str:
        pizzas = data["pizza_name"].unique().tolist()
        while True:
            self.nombre_elegido = input(f"Elige la pizza que deseas entre {pizzas}: ")
            if self.nombre_elegido in pizzas:
                return self.nombre_elegido
            else:
                print("Pizza no disponible")
                return self.nombre()
        
    def precio(self) -> float:
        pizza_escogida = self.nombre_elegido
        precio = data[data["pizza_name"] == pizza_escogida]["total_price"].unique()
        return precio[0]'''





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

    def is_composite(self) -> bool:
        return True
    
    def nombre(self) -> str:
        return "Menu"

    def precio(self) -> float:
        """
        The Composite executes its primary logic in a particular way. It
        traverses recursively through all its children, collecting and summing
        their results. Since the composite's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result.
        """

        total_price = 0
        for child in self._children:
            total_price += child.precio()
        return total_price

def client_code(component: List[Menu]) -> None:   #menu simple
    """
    The client code works with all of the components via the base interface.
    """
    print(f"Nombre: {component.nombre()}")
    print(f"Precio: {component.precio()}")



if __name__ == "__main__":
    entrante = Entrante()
    pizza = Pizza()

    print("Elige tu comida:")
    client_code(entrante)
    client_code(pizza)

    menu = Composite()
    menu.add(entrante)
    menu.add(pizza)

    print("El menú:")
    client_code(menu)

