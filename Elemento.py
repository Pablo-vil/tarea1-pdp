from typing import Dict, Any
from TipoElemento import TipoElemento

class Elemento:
    def __init__(self, tipo: TipoElemento, tiempo_creacion: float):
        self.tipo: TipoElemento = tipo
        self.tiempo_creacion: float = tiempo_creacion
        self.caracteristicas: Dict[str, Any] = {}
        self.id_elemento: int = 0


    def asignar_caracteristica(self, nombre: str, valor: Any):
        if nombre in self.tipo.caracteristicas_posibles:
            if valor in self.tipo.caracteristicas_posibles[nombre]:
                self.caracteristicas[nombre] = valor
            else:
               print(f"valor {valor} no valido para caracteristica {nombre}")
        else:
            print(f"caracteristica {nombre} no existe en tipo {self.tipo.nombre}")
    
    def obtener_caracteristica(self, nombre: str) -> Any:
        return self.caracteristicas.get(nombre, None)