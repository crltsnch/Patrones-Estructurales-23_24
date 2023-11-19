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