from __future__ import annotations
import pandas as pd
from codigocliente import client_code
from hojas import Entrante, Pizza, Bebida, Postre
from composite import CompositeCombo, CompositeComboCompuesto
from guardarmenus import guardar_menu_personalizado

data = pd.read_csv('/Users/carlotasanchezgonzalez/Documents/class/Patrones-Estructurales-23_24/Ejercicio 1/pizzas/data/data_final.csv', sep=';', encoding='ISO-8859-1')

if __name__ == "__main__":
    """
    This way the client code can support the simple leaf components...
    """
    print("Bienvenido a la pizzeria")
    print("¿Quieres crear tu propio menu o elegir uno ya hecho?")
    
    opciones = [1, 2]
    mensaje = "1. Crear menu \n2. Elegir menu ya hecho \nElige una opción: "
    eleccion = client_code(mensaje, opciones)



    if eleccion == 1:
        print("¡Vamos a crear tu menu!")

        # Generar instancias de Entrante con todos los entrantes y precios disponibles
        entrantes_disponibles = [
             ("salsa cesar", 3.5),
            ("alitas de pollo a la parrilla", 5.5),
            ("nachos", 6.5),
            ("mini calzones", 4.5),
            ("rollitos de primavera caprese", 7.5)
        ]
        instancias_entrantes = [Entrante(nombre, precio) for nombre, precio in entrantes_disponibles]

        # Generar instancias de Pizza con todos los nombres y precios disponibles
        pizzas_disponibles = data.groupby('pizza_name')['total_price'].first().reset_index()
        instancias_pizzas = [Pizza(nombre, precio) for nombre, precio in pizzas_disponibles.values]

        #Generar instancias de Bebida con todos los nombres y precios disponibles  
        bebidas_disponibles = [
            ("Garnacha", 2.5),
            ("Chardonnay", 3.5),
            ("Viura", 3.5),
            ("Albariño", 4.5),
            ("Cerveza de trigo", 3),
            ("Cerveza rubia", 3.5),
            ("Cerveza tostada", 3.5),
            ("Cerveza con limón", 3),
            ("Limonada Casera", 2.5),
            ("Agua", 1.5),
            ("Agua con gas", 1.7),
            ("Cola", 2),
            ("Leche", 2)
        ]
        instancias_bebidas = [Bebida(nombre, precio) for nombre, precio in bebidas_disponibles]


        #Generar instacias de Postre con todos los nombres y precios disponibles
        postres_disponibles = [
            ("Tarta de queso", 5.5),
            ("Mousse de chocolate", 4.5),
            ("Tarta de zanahoria", 4.5),
            ("Helado variado", 3.5),
            ("Tiramisu", 5.5)
        ]


        # Permitir al cliente elegir su menu dandole a elegir entre los entrantes mediante un numero
        print("\nEntrantes disponibles:")
        for i, entrante in enumerate(instancias_entrantes, start=1):
            print(f"{i}. {entrante.nombre} - Precio: {entrante.precio}")

        eleccion_entrante = client_code("Elige un entrante (número): ", list(range(1, len(instancias_entrantes) + 1)))
        entrante_personalizado = instancias_entrantes[eleccion_entrante - 1]

        # Permitir al cliente elegir su menu dandole a elegir entre las pizzas disponibles mediante un numero
        print("\nPizzas disponibles:")
        for i, pizza in enumerate(instancias_pizzas, start=1):
            print(f"{i}. {pizza.nombre} - Precio: {pizza.precio}")

        eleccion_pizza = client_code("Elige una pizza (número): ", list(range(1, len(instancias_pizzas) + 1)))
        pizza_personalizada = instancias_pizzas[eleccion_pizza - 1]

        # Permitir al cliente elegir su menu dandole a elegir entre las bebidas disponibles mediante un numero
        print("\nBebidas disponibles:")
        for i, bebida in enumerate(instancias_bebidas, start=1):
            print(f"{i}. {bebida.nombre} - Precio: {bebida.precio}")
        
        eleccion_bebida = client_code("Elige una bebida (número): ", list(range(1, len(instancias_bebidas) + 1)))
        bebida_personalizada = instancias_bebidas[eleccion_bebida - 1]

        # Permitir al cliente elegir su menu dandole a elegir entre los postres disponibles mediante un numero
        print("\nPostres disponibles:")
        for i, (nombre_postre, precio_postre) in enumerate(postres_disponibles, start=1):
            print(f"{i}. {nombre_postre} - Precio: {precio_postre}")

        eleccion_postre = client_code("Elige un postre (número): ", list(range(1, len(postres_disponibles) + 1)))
        nombre_postre, precio_postre = postres_disponibles[eleccion_postre - 1]
        postre_personalizado = Postre(nombre_postre, precio_postre)

        # Crear menú personalizado
        nombre_combo = input("Elige un nombre para tu combo: ")
        menu_personalizado = CompositeCombo(nombre_combo)
        menu_personalizado.add(entrante_personalizado)
        menu_personalizado.add(pizza_personalizada)
        menu_personalizado.add(bebida_personalizada)
        menu_personalizado.add(postre_personalizado)

        print("\nMenú Personalizado:")
        menu_personalizado.mostrar()
        

        # Guardar menú personalizado
        guardar_menu_personalizado(menu_personalizado)



    elif eleccion == 2:
        print("¡Vamos a elegir un menu de nuestras creaciones!\n")
        
        '''----------Combo Predefinido 1----------'''
        #Creamos las intancias de entrantes y pizzas para añadir a nuestro combo individual prefenido
        entrante1 = Entrante("salsa cesar", 3.5)
        pizza1 = Pizza("The Mediterranean Pizza", data[data["pizza_name"] == "The Mediterranean Pizza"]["total_price"].unique()[0])
        bebida1 = Bebida("Cola", 2.5)
        postre1 = Postre("Tarta de queso", 5.5)


        #Creamos el combo
        combo1 = CompositeCombo("Combo Individual")
        combo1.add(entrante1)
        combo1.add(pizza1)
        combo1.add(bebida1)
        combo1.add(postre1)

        print("Combo Individual")
        combo1.mostrar()

        descuento = 0.2
        precio_descuento1 = combo1.precio_total() * (1 - descuento)
        print("\n¡Oferta especial! Al elegir este combo obtienes un 20% de descuento:")
        print(f"Combo Individual precio final con descuento: {round(precio_descuento1, 2)}\n")


        '''----------Combo Predefinido 2----------'''
        pizza2 = Pizza("The Prosciutto and Arugula Pizza", data[data["pizza_name"] == "The Prosciutto and Arugula Pizza"]["total_price"].unique()[0])
        postre2 = Postre("Tiramisu", 5.5)

        combo2 = CompositeCombo("Combo Sencillo")
        combo2.add(pizza2)
        combo2.add(postre2)

        print("Combo Sencillo")
        combo2.mostrar()

        descuento = 0.1
        print("\n¡Oferta especial! Al elegir este combo obtienes un 10% de descuento:")
        precio_descuento2 = combo2.precio_total() * (1 - descuento)
        print(f"Combo Sencillo precio final con descuento: {round(precio_descuento2, 2)}\n")


        '''----------Combo Predefinido 3----------'''
        entrante3 = Entrante("nachos", 5.5)
        pizza3 = Pizza("The Thai Chicken Pizza", data[data["pizza_name"] == "The Thai Chicken Pizza"]["total_price"].unique()[0])
        bebida3 = Bebida("Albariño", 4.5)
        postre3 = Postre("Mousse de chocolate", 4.5)

        combo3 = CompositeCombo("Combo Deluxe")
        combo3.add(entrante3)
        combo3.add(pizza3)
        combo3.add(bebida3)
        combo3.add(postre3)

        print("Combo Deluxe")
        combo3.mostrar()


        descuento = 0.2
        precio_descuento3 = combo3.precio_total() * (1 - descuento)
        print("\n¡Oferta especial! Al elegir este combo obtienes un 20% de descuento:")
        print(f"Combo Individual precio final con descuento: {round(precio_descuento3, 2)}\n")




        '''----------Combo Compuesto 1----------'''
        # Creamos un combo compuesto con el combo1 y combo2 con descuento
        combo_compuesto1 = CompositeComboCompuesto("Combo Pareja")
        combo_compuesto1.personalizar(combo1, combo2)
        combo_compuesto1.mostrar()

        descuento = 0.3
        precio_descuento2 = combo_compuesto1.precio_total() * (1 - descuento)
        print("\n¡Oferta especial! Al elegir este combo obtienes un 30% de descuento:")
        print(f"Combo Pareja precio final con descuento: {round(precio_descuento2, 2)}\n")

        '''----------Combo Compuesto 2----------'''
        # Creamos un combo compuesto con el combo1 y combo3 con descuento
        combo_compuesto2 = CompositeComboCompuesto("Combo Familiar")
        combo_compuesto2.personalizar(combo1, combo3)
        combo_compuesto2.mostrar()

        descuento = 0.1
        precio_descuento2 = combo_compuesto1.precio_total() * (1 - descuento)
        print("\n¡Oferta especial! Al elegir este combo obtienes un 10% de descuento y gana 2 entradas para el cine:")
        print(f"Combo Pareja precio final con descuento: {round(precio_descuento2, 2)}\n")





        '''----------Selección de Combo----------'''
        while True:
            print("1. Combo Individual")
            print("2. Combo Sencillo")
            print("3. Combo Deluxe")
            print("4. Combo Pareja")
            print("5. Combo Familiar")
            combo_elegido = int(input("¿Qué combo deseas? (número) o deseas salir (6): "))
            combos = [1, 2, 3, 4, 5, 6]

            if combo_elegido not in combos:
                print("Opción no disponible")
                continue
            
            if combo_elegido == 6:
                break

            
            print("¡Gracias por elegirnos!")
            print("Tu pedido está en marcha...")
            print("¡Buen provecho!")
            break
                

    else:
        print("Opción no válida. Vuelve a intentarlo.")

