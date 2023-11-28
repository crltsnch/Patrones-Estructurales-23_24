from __future__ import annotations
from componente import Component
from typing import List
from hojas import Documento, Link


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
        self.accesos_registrados: List[str] = []

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
    
    def modificar(self, nombre_documento: str, nuevo_nombre: str) -> None:
        """
        Modificar el nombre de un componente en la carpeta y sus subcarpetas si es necesario.
        """
        for child in self._children:
            if isinstance(child, Carpeta) and child.is_composite():
                child.modificar(nombre_documento, nuevo_nombre)
            elif isinstance(child, Documento) and child.nombre == nombre_documento:
                child.modificar(nuevo_nombre)
                print(f"Modificado en '{self.nombre}': {child.mostrar()}")

    def acceder(self, usuario: str) -> None:
        registro = f"Registro de acceso por {usuario} a la carpeta {self.nombre}"
        self.accesos_registrados.append(registro)
        print(registro) 
