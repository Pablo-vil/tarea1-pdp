from typing import Dict, Any, List

class TipoElemento:
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.caracteristicas_posibles: Dict[str, List[Any]] = {}
    
    def agregar_caracteristica(self, nombre_caracteristica: str, valores_posibles: List[Any]):

        self.caracteristicas_posibles[nombre_caracteristica] = valores_posibles
    
    def obtener_caracteristicas(self) -> Dict[str, List[Any]]:
        
        return self.caracteristicas_posibles