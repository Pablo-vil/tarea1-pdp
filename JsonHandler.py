import json
from typing import Dict, List, Tuple, Any
from Proceso import Proceso

class JsonHandler:
    def __init__(self):
        self.path: str = ""
        self.data: Dict[str, Any] = {}

    def verificarJson(self, archivo: str) -> bool:

        campos_necesarios = ("name", "components", "connections")

        try:
            with open(archivo, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
            
            for campo in campos_necesarios:
                if campo not in self.data:
                    print(f"Falta el campo requerido: {campo}")
                    return False
            return True

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error al leer el archivo JSON: {e}")
            return False


    def cargar_json(self, proceso: Proceso) -> bool:
        archivo = input("ingrese el archivo a leer: ")
        self.path = archivo

        if not self.verificarJson(self.path):
            return False
                    
        proceso.name =          self.data.get("name", "sin_nombre")
        proceso.element_types = self.data.get("element_types", [])
        proceso.components =    self.data.get("components", [])
        proceso.connections =   self.data.get("connections", [])

        print(f"Tipo de components: {type(proceso.components)}")
        if proceso.components:
            print(f"Tipo del primer componente: {type(proceso.components[0])}")
            print(f"Primer componente: {proceso.components[0]}")
        return True

    
    def guardar_json(self, proceso: Proceso) -> bool:
        if not proceso.name:
            print("No hay datos para guardar")
            return False
            
        nombre_archivo = input("Nombre del archivo (sin .json): ")
        if not nombre_archivo.strip():
            print("Nombre de archivo no puede estar vacio")
            return False
            
        try:

            datos_actualizados = self.data.copy()
            datos_actualizados['name'] = proceso.name
            datos_actualizados['components'] = proceso.components
            datos_actualizados['element_types'] = proceso.element_types
            datos_actualizados['connections'] = proceso.connections
            
            with open(f"{nombre_archivo}.json", 'w', encoding='utf-8') as file:
                json.dump(datos_actualizados, file, ensure_ascii=False, indent=4)
            print(f"Archivo guardado como {nombre_archivo}.json")
            return True
        
        except Exception as e:
            print(f"Error al guardar: {e}")
            return False