from .Componente import Componente

class Sink(Componente):
    def __init__(self, nombre: str, id: str):
        super().__init__(id=id, nombre=nombre, tipo_componente="sink")
        self.tiempo_procesamiento = 0
