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
        self.assertEqual(entrante.mostrar(), "Entrante: salsa cesar , Precio: 3.5")
    
    def test_pizza(self):
        pizza = Pizza("The Mediterranean Pizza", 12.5)
        self.assertEqual(pizza.mostrar(), "Pizza: The Mediterranean Pizza , Precio: 12.5")
    
    def test_bebida(self):
        bebida = Bebida("Cola", 2.5)
        self.assertEqual(bebida.mostrar(), "Bebida: Cola , Precio: 2.5")
    
    def test_postre(self):
        postre = Postre("Tarta de queso", 4.5)
        self.assertEqual(postre.mostrar(), "Postre: Tarta de queso , Precio: 4.5")
    
    def test_composite_combo(self):
        combo = CompositeCombo("Combo 1")
        entrante = Entrante("salsa cesar", 3.5)
        pizza = Pizza("The Mediterranean Pizza", 12.5)
        bebida = Bebida("Cola", 2.5)
        postre = Postre("Tarta de queso", 4.5)

        combo.add(entrante)
        combo.add(pizza)
        combo.add(bebida)
        combo.add(postre)

        with patch("sys.stdout") as mock_stdout:
            combo.mostrar()
            expected_output = "Combo: Combo 1\nEntrante: salsa cesar , Precio: 3.5\nPizza: The Mediterranean Pizza , Precio: 12.5\nBebida: Cola , Precio: 2.5\nPostre: Tarta de queso , Precio: 4.5\n"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
        

    def test_composite_combo_compuesto(self):
        combo_compuesto = CompositeComboCompuesto("Combo Compuesto")
        combo1 = CompositeCombo("Combo 1")
        combo2 = CompositeCombo("Combo 2")

        entrante = Entrante("salsa cesar", 3.5)
        pizza = Pizza("The Mediterranean Pizza", 12.5)
        bebida = Bebida("Cola", 2.5)
        postre = Postre("Tarta de queso", 4.5)

        combo1.add(entrante)
        combo1.add(pizza)
        combo1.add(bebida)
        combo1.add(postre)

        combo2.add(pizza)
        combo2.add(postre)

        combo_compuesto.personalizar(combo1, combo2)

        with patch("sys.stdout") as mock_stdout:
            combo_compuesto.mostrar()
            expectes_output = "Combo Compuesto: combo_compuesto\nCombo: Combo1\nEntrante: salsa cesar , Precio: 3.5\nPizza: The Mediterranean Pizza , Precio: 12.5\nBebida: Cola , Precio: 2.5\nPostre: Tarta de queso , Precio: 4.5\nCombo: Combo 2\nPizza: The Mediterranean Pizza , Precio: 12.5\nPostre: Tarta de queso , Precio: 4.5\nPrecio total del Combo: 40.0\n\nCombo: Combo2\nPizza: The Mediterranean Pizza , Precio: 12.5\nPostre: Tarta de queso , Precio: 4.5\nPrecio total del Combo: 17.0\n\nPrecio total del Combo Compuesto: 57.0\n"
            self.assertEqual(mock_stdout.getvalue().strip(), expectes_output)
    
    def test_client_code(self):
        #Prueba la función de entrada del usuario con entrada válida
        with patch("builtins.input", return_value="1"):
            self.assertEqual(client_code("Elige un postre (número): ", list(range(1, 3))), 1)
        
        #Prueba la función de entrada del usuario con entrada inválida
        with patch("builtins.input", side_effect=["invalid", "3"]):
            self.assertEqual(client_code("Elige un postre (número): ", list(range(1, 3))), 3)
