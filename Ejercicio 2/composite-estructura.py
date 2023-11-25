from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    The base Component class declares common operations for both simple and
    complex objects of a composition.
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def mostrar(self) -> str:
        pass

    def get_tamaño(self) -> int:
        pass

    def acceder(self, usuario:str) -> None:
        pass


class Documento(Component):
    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.

    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-components.
    """
    def __init__(self, nombre: str, tipo:str, tamaño:int, sensible: bool = False):
        self.nombre = nombre
        self.tipo = tipo
        self.tamaño = tamaño
        self.sensible = sensible

    def mostrar(self) -> str:
        return f"Document: {self.nombre} {self.tipo} {self.tamaño}"
    
    def get_tamaño(self) -> int:
        return self.tamaño


class Link(Component):
    def __init__(self, target: str, tamaño_simbolico: int=0):
        self.target = target
        self.tamaño_simbolico = tamaño_simbolico

    def mostrar(self) -> str:
        return f"Link: {self.target} {self.tamaño_simbolico}"
    
    def get_tamaño(self) -> int:
        return self.tamaño_simbolico


class Carpeta(Component):
    """
    The Composite class represents the complex components that may have
    children. Usually, the Composite objects delegate the actual work to their
    children and then "sum-up" the result.
    """

    def __init__(self, nombre: str):
        self.nombre = nombre
        self._children: List[Component] = []
        self._tamaño = 0

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self
        self._tamaño += component.get_tamaño()

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None
        self._tamaño -= component.get_tamaño()

    def is_composite(self) -> bool:
        return True

    def mostrar(self) -> str:
        results = []
        for child in self._children:
            results.append(child.mostrar())
        return f"Carpeta: {self.nombre} ({', '.join(results)}) {self._tamaño} bytes"

    def get_tamaño(self) -> int:
        return sum([child.get_tamaño() for child in self._children])


def client_code(component: Component) -> None:
    """
    The client code works with all of the components via the base interface.
    """
    print(f"RESULT:\n{component.mostrar()}", end="\n")



if __name__ == "__main__":
    ruta_carpeta = Carpeta("Ruta")
    carpeta1 = Carpeta("Carpeta1")
    carpeta2 = Carpeta("Carpeta2")
    documento1 = Documento("Documento1.txt", "txt", 1100)
    documento2 = Documento("img.jpg", "image", 1200)
    link1 = Link("Link to Carpeta2", tamaño_simbolico=10)

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