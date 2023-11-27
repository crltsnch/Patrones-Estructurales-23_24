from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from registros import logger

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
    def mostrar(self) -> dict:
        pass

    def get_tamaño(self) -> int:
        pass

    def acceder(self) -> None:
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

    def mostrar(self) -> dict:
        return {
                "nombre": self.nombre,
                "tipo": self.tipo,
                "tamano": self.tamaño
                }
    
    def get_tamaño(self) -> int:
        return self.tamaño

    @logger
    def acceder(self, usuario: str) -> None:
        print(f"Acceso a {usuario} al documemnto {self.nombre}")


class Link(Component):
    def __init__(self, target: str, tamaño: int=0):
        self.target = target
        self.tamaño = tamaño

    def mostrar(self) -> dict:
        return {
            "target": self.target,
            "tamano": self.tamaño
            }
    
    def get_tamaño(self) -> int:
        return self.tamaño

    def acceder(self, usuario: str) -> None:
        self.target.acceder(usuario)


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

    def mostrar(self) -> dict:
        return {
            "type": self.__class__.__name__,
            "nombre": self.nombre,
            "children": [child.mostrar() for child in self._children],
            "tamano": self.get_tamaño()
        }

    def get_tamaño(self) -> int:
        return sum([child.get_tamaño() for child in self._children])
    
    def acceder(self, usuario: str) -> None:
        print(f"Registro de acceso por {usuario} a la carpeta {self.nombre}")


def client_code(component: Component) -> None:
    """
    The client code works with all of the components via the base interface.
    """
    print(f"RESULT:\n{component.mostrar()}", end="\n")