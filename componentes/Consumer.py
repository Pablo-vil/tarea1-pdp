from .Componente import Componente

class Consumer(Componente):
    def __init__(self, nombre: str, id: str):
        super().__init__(id=id, nombre=nombre, tipo_componente="consumer")
        self.tiempo_consumo = 0
