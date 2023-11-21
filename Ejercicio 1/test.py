import unittest
from unittest.mock import patch
from codigocliente import client_code
from hojas import Entrante, Pizza, Bebida, Postre
from composite import CompositeCombo, CompositeComboCompuesto

'''Pruebas unitarias que cubran casos básicos.
Cobertura de casos de borde y validación de correcta funcionalidad en diferentes escenarios'''

class TestMenus(unittest.TestCase):
    def test_entrante(self):
        entrante = Entrante("salsa cesar", 3.5)
        self.assertEqual(entrante.mostrar, "Entrante: salsa cesar - Precio: 3.5")
        