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