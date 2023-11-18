from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Menu(ABC):
    """
    The base Component class declares common operations for both simple and
    complex objects of a composition.
    """

    @property
    def parent(self) -> Menu:
        return self._parent

    @parent.setter
    def parent(self, parent: Menu):
        """
        Optionally, the base Component can declare an interface for setting and
        accessing a parent of the component in a tree structure. It can also
        provide some default implementation for these methods.
        """

        self._parent = parent

    """
    In some cases, it would be beneficial to define the child-management
    operations right in the base Component class. This way, you won't need to
    expose any concrete component classes to the client code, even during the
    object tree assembly. The downside is that these methods will be empty for
    the leaf-level components.
    """

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
    def nombre(self) -> str:
        pass

    @abstractmethod
    def precio(self) -> float:
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

    def operation(self) -> str:
        """
        The Composite executes its primary logic in a particular way. It
        traverses recursively through all its children, collecting and summing
        their results. Since the composite's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result.
        """

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


def client_code(component: Menu) -> None:   #menu simple
    """
    The client code works with all of the components via the base interface.
    """

    print(f"RESULT: {component.operation()}", end="")


def client_code2(component1: Menu, component2: Menu) -> None:   #menu compuesto
    """
    Thanks to the fact that the child-management operations are declared in the
    base Component class, the client code can work with any component, simple or
    complex, without depending on their concrete classes.
    """

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


if __name__ == "__main__":
    # This way the client code can support the simple leaf components...
    simple = Entrante()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as the complex composites.
    tree = Composite()   #menu compuesto con menus simples

    branch1 = Composite()
    branch1.add(Entrante())
    branch1.add(Entrante())

    branch2 = Composite()
    branch2.add(Entrante())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)