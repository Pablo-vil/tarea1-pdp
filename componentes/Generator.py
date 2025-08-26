from rich.console import Console
from rich.prompt import Prompt
from .Componente import Componente

class Generator(Componente):
    def __init__(self, nombre: str, id: str):
        super().__init__(id=id, nombre=nombre, tipo_componente="generator")
        self.intervalo = 0
        self.elementosCreados=0
        self.elementosMax=0

        