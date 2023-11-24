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


class Document(Component):
    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.

    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-components.
    """
    def __init__(self, nombre: str, tipo:str, tamaño:int):
        self.nombre = nombre
        self.tipo = tipo
        self.tamaño = tamaño

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
        return f"Folder: {self.nombre} ({', '.join(results)}) {self._tamaño} bytes"


def client_code(component: Component) -> None:
    """
    The client code works with all of the components via the base interface.
    """

    print(f"RESULT: {component.mostrar()}", end="\n")



if __name__ == "__main__":
    # This way the client code can support the simple leaf components...
    simple = Leaf()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as the complex composites.
    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)