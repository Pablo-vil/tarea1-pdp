from typing import Any
from componentes.Generador import Generador

class Proceso:
    def __init__(self, nombre):
        self.name:str = nombre
        self.element_types = []
        self.components = []
        self.connections = []

    ## setters
    def setNombre(self):
        nombreNuevo:str = input("Ingrese un nuevo nombre")
        self.nombre = nombreNuevo
            
    
    ## getters

    def getNombre(self):
        return(self.nombre)
    
    def getComponentes(self):
        return(self.components)
