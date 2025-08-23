from typing import Any
from componentes/Generador import Generador

class Proceso:
    def __init__(self, nombre):
        self.nombre:str = nombre
        self.componentes: dict[str, Any] = {}


    ## setters
    def setNombre(self):
        nombreNuevo:str = input("Ingrese un nuevo nombre")
        self.nombre = nombreNuevo

    def setComponentes(self):

        opciones = [
            "1. Generador",
            "2. Fila",
            "3. Seleccionador",
            "4. Transportador",
            "5. Consumidor/Transformador",
            "6. Salidas"
            "7. Terminar"
            "\n"
        ]

        print("Ingrese los componentes como un diccionario (por ejemplo: {'clave': 'valor'}): ")
        print("primero ingreser el tipo y luego la cantidad")

        entrada = 0
        while(entrada != 7):
            for opcion in opciones:
                print(opcion)

            entrada = input("ingrese una de las opciones")
            if entrada == 1:
                cantidad = int(input("Cuantos generadores quiere agregar? "))
                for i in range(cantidad):
                    nombre = input(f"Nombre del generador {i+1}: ")
                    gen = Generador(nombre)
                print(f"{cantidad} generador(es) agregado(s)")
                
            elif entrada == 2:
                cantidad = int(input("Cuantas filas quiere agregar? "))
                for i in range(cantidad):
                    nombre = input(f"Nombre de la fila {i+1}: ")
                    # Crear y agregar fila
                print(f"{cantidad} fila(s) agregada(s)")
                
            elif entrada == 3:
                cantidad = int(input("Cuantos seleccionadores quiere agregar? "))
                for i in range(cantidad):
                    nombre = input(f"Nombre del consumidor {i+1}: ")
                    # Crear y agregar consumidor
                print(f"{cantidad} consumidor(es) agregado(s)")
                
            elif entrada == 4:
                cantidad = int(input("Cuantos transportadores quiere agregar? "))
                for i in range(cantidad):
                    nombre = input(f"Nombre de la salida {i+1}: ")
                    # Crear y agregar salida
                print(f"✓ {cantidad} salida(s) agregada(s)")
                
            elif entrada == 5:
                cantidad = int(input("Cuantos Consumidor/Transformador quiere agregar? "))
                for i in range(cantidad):
                    nombre = input(f"Nombre de la salida {i+1}: ")
                    # Crear y agregar salida
                print(f"✓ {cantidad} salida(s) agregada(s)")

            elif entrada == 6:
                cantidad = int(input("Cuantas Salidas quiere agregar? "))
                for i in range(cantidad):
                    nombre = input(f"Nombre de la salida {i+1}: ")
                    # Crear y agregar salida
                print(f"✓ {cantidad} salida(s) agregada(s)")

            elif entrada == 7:
                break

            else:
                print("❌ Opción no válida")


            
    
    ## getters

    def getNombre(self):
        return(self.nombre)
    
    def getComponentes(self):
        return(self.componentes)
