from typing import Dict, Any
from TipoElemento import TipoElemento

class Elemento:
    def __init__(self, tipo: TipoElemento, tiempo_creacion: float):
        self.tipo: TipoElemento = tipo
        self.tiempo_creacion: float = tiempo_creacion
        self.caracteristicas: Dict[str, Any] = {}
        self.id_elemento: int = 0

    
    


    def obtener_caracteristica(self, nombre: str) -> Any:
        return self.caracteristicas.get(nombre, None)