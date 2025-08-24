from typing import Dict, Any, List
import json

class TipoElemento:
    def __init__(self, id: str, nombre: str):
        self.id: str= id
        self.name: str = nombre
        self.atributes: List[Dict[str, Any]] = []
        self.caracteristicas_posibles: Dict[str, List[Any]] = {}


    def obtenerDatosJson(self):
        inputFile = input("Ingrese el camino del archivo a leer: ")
        with open("archivo.json", 'r', encoding='utf-8') as file:
            datos = json.load(file)
        