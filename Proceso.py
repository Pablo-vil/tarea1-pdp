from typing import Any
from componentes.Generador import Generador
import json

class Proceso:
    def __init__(self, nombre):
        self.name:str = nombre
        self.element_types = []
        self.components = []
        self.connections = []
        self.datos_json = {}

    ## setters
    def setNombre(self):
        nombreNuevo:str = input("Ingrese un nuevo nombre")
        self.nombre = nombreNuevo

    
    ## getters

    def getNombre(self):
        return(self.nombre)
    
    def getComponentes(self):
        return(self.components)


    ## aparte

    def cargar_json(self):
        archivo = input("ingrese el archivo a leer: ")
        with open(archivo, 'r', encoding='utf-8') as file:
                data = json.load(file)
                    
        self.name = data.get("name", "sin_nombre")
        self.datos_json = data
        self.element_types = data.get("element_types", [])
        self.components = data.get("components", [])
        self.connections = data.get("connections", [])

        print(self.datos_json)

    def mostrar_componentes(self):

        print("\nComponentes:")
        for i, comp in enumerate(self.components, 1):
            nombre = comp.get("name", "sin_nombre")
            tipo = comp.get("type", "sin_tipo")
            print(f"  {i}. {nombre} ({tipo})")

    def obtener_componente(self, indice: int):
        if 1 <= indice <= len(self.components):
            return self.components[indice - 1]
        return None