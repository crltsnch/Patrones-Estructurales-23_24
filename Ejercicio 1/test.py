import unittest
from unittest.mock import patch
from codigocliente import client_code
from hojas import Entrante, Pizza, Bebida, Postre
from composite import CompositeCombo, CompositeComboCompuesto

'''Pruebas unitarias que cubran casos básicos.
Cobertura de casos de borde y validación de correcta funcionalidad en diferentes escenarios'''

class TestMenuPizzeria(unittest.TestCase):
    def test_menu_personalizado(self):
        #Probando crear un menú personalizado proporcionando entrada a la función client_code
        entrada_usuario = iter(['1', '1', '1', '1', '1', 'Mi Combo Personalizado'])
        with self.assertRaises(SystemExit):
            with patch('builtins.input', lambda: next(entrada_usuario)):
                client_code("Elige una opción: ", [1, 2])

    def test_menu_predefinido(self):
        #Probando crear un menú predefinido proporcionando entrada a la función client_code
        entrada_usuario = iter(['2', '1'])
        with self.assertRaises(SystemExit):
            with patch('builtins.input', lambda: next(entrada_usuario)):
                client_code("Elige una opción: ", [1, 2])

