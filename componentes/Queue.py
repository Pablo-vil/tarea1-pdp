from .Componente import Componente

class Fila(Componente):
    def __init__(self, nombre: str, id: str):
        super().__init__(id=id, nombre=nombre, tipo_componente="queue")
        self.disciplina = ""
        self.capacidad = 0