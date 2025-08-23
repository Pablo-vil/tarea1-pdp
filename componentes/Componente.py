class Componente:
    def __init__(self, id: str, nombre: str, tipo_componente: str):
        self.id = id
        self.nombre: str = nombre
        self.tipo_componente: str = tipo_componente
        self.io = {}
        self.params = {}


    def obtenerDatos(self) -> str:
        
        return f"{self.tipo_componente}: {self.nombre}"
    