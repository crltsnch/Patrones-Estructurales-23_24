from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import pandas as pd

data = pd.read_csv('/Users/carlotasanchezgonzalez/Documents/class/Patrones-Estructurales-23_24/Ejercicio 1/data/data_final.csv', sep=';', encoding='ISO-8859-1')

class Menu(ABC):
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
    
    def mostrar(self) -> str:
        pass



class Entrante(Menu):
    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.

    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-components.
    """

    def nombre(self) -> str:
        entrantes = ["salsa cesar", "alitas de pollo a la parrilla", "nachos", "mini calzones", "rollitos de primavera caprese"]
        entrante = input(f"Elige un entrante de  {entrantes}: ")
        if entrante not in entrantes:
            print("Entrante no disponible")
            return self.nombre()
        else:
            return entrante
    
    def precio(self) -> float:
        precios = [3.5, 5.5, 6.5, 4.5, 7.5]
        entrante = self.nombre()
        if entrante == "salsa cesar":
            return precios[0]
        elif entrante == "alitas de pollo a la parrilla":
            return precios[1]
        elif entrante == "nachos":
            return precios[2]
        elif entrante == "mini calzones":
            return precios[3]
        elif entrante == "rollitos de primavera caprese":
            return precios[4]

class Pizza(Menu):

    def nombre(self) -> str:
        pizzas = data["pizza_name"].unique().tolist()
        pizza_escogida = input(f"Elige la pizza que deseas entre {pizzas}: ")
        if pizza_escogida not in pizzas:
            print("Pizza no disponible")
            return self.nombre()
        else:
            return pizza_escogida
        
    def precio(self) -> float:
        pizza_escogida = self.nombre()
        precio = data[data["pizza_name"] == pizza_escogida]["total_price"].unique()
        return precio[0]


class Composite(Menu):
    """
    The Composite class represents the complex components that may have
    children. Usually, the Composite objects delegate the actual work to their
    children and then "sum-up" the result.
    """

    def __init__(self) -> None:
        self._children: List[Menu] = []

    """
    A composite object can add or remove other components (both simple or
    complex) to or from its child list.
    """

    def add(self, component: Menu) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Menu) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

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

    def __iter__(self):
        return iter(self._children)

def client_code(components: List[Menu]) -> None:   #menu simple
    """
    The client code works with all of the components via the base interface.
    """
    
    for component in components:
        if isinstance(component, Composite):
            print("Composite Menu:")
            client_code(component._children)
        else:
            print(f"Nombre: {component.nombre()}", end="")
            print(f"Precio: {component.precio()}", end="")


if __name__ == "__main__":
    entrante = Entrante()
    pizza = Pizza()

    print("Cliente: Elige tu comida:")
    entrante.nombre()
    pizza.nombre()

    print(f"Nombre del entrante: {entrante.nombre()}")
    print(f"Nombre de la pizza: {pizza.nombre()}")

    total_precio = entrante.precio() + pizza.precio()
    print(f"Precio total: {total_precio}")

