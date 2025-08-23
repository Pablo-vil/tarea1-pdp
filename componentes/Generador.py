from rich.console import Console
from rich.prompt import Prompt
from Elemento import Elemento
from TipoElemento import TipoElemento

class Generador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.intervalo = 0
        self.elementosCreados=0
        self.elementosMax=0

        