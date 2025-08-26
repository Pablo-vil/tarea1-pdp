from rich.console import Console
from rich.prompt import Prompt
from Elemento import Elemento
from TipoElemento import TipoElemento
from .Componente import Componente

class Generador(Componente):
    def __init__(self, nombre: str, id: str):
        super().__init__(id=id, nombre=nombre, tipo_componente="generador")
        self.intervalo = 0
        self.elementosCreados=0
        self.elementosMax=0

        