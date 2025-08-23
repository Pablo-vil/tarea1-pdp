class Componente:
    def __init__(self, nombre: str, tipo_componente: str):
        self.nombre: str = nombre
        self.tipo_componente: str = tipo_componente  # "generador", "fila", etc.
        self.entradas: list = []
        self.salidas: list = []
    
    def conectarSalida(self, otro_componente: 'Componente'):
        """Conecta este componente con otro (este → otro)"""
        if otro_componente not in self.salidas:
            self.salidas.append(otro_componente)
        if self not in otro_componente.entradas:
            otro_componente.entradas.append(self)
    
    def obtenerDatos(self) -> str:
        
        return f"{self.tipo_componente}: {self.nombre}"
    