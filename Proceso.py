from typing import Any, List, Dict
from componentes.Generator import Generator
import json

class Proceso:
    def __init__(self, nombre):
        self.name:str = nombre
        self.element_types = []
        self.components: List[Dict[str, Any]] = []
        self.connections = []

    def __repr__(self) -> str:
        string = ""

        n_types = len(self.element_types)
        n_components = len(self.components)
        n_connections = len(self.connections)

        string = (f"""proceso {self.name}, num de tipos: {n_types},num de componentes: {n_components}, num de conecciones: {n_connections}
                  """)
        string += ("componentes: \n")
        for componente in self.components:

            id_comp = componente.get("id")
            tipo_comp = componente.get("type")
            name_comp = componente.get("name")
            io_comp = componente.get("io")
            params_comp = componente.get("params", {})


            string += (f"""  id: {id_comp}, nombre: {name_comp}\n
                          tipo: {tipo_comp}
                       \n""")
                          ## io: {io_comp}
                          ## params: {params_comp} 

        if self.connections:

            string += "conexiones:\n"
            for con in self.connections:
                desde_con = con.get("from")
                hasta_con = con.get("to")
                string += f"  {desde_con} → {hasta_con}\n"



        return string

    ## setters
    def setNombre(self):
        nombreNuevo:str = input("Ingrese un nuevo nombre")
        self.name = nombreNuevo

    
    ## getters

    def getNombre(self):
        return(self.name)
    
    def getComponentes(self):
        return(self.components)


    ## aparte

    

    def cargar_json(self):
        archivo = input("ingrese el archivo a leer: ")
        with open(archivo, 'r', encoding='utf-8') as file:
                data = json.load(file)
                    
        self.name = data.get("name", "sin_nombre")
        self.element_types = data.get("element_types", [])
        self.components = data.get("components", [])
        self.connections = data.get("connections", [])

        print(data)

    def mostrar_componentes(self):

        print("\nComponentes:")
        for i, comp in enumerate(self.components, 1):
            nombre = comp.get("name", "NA")
            tipo = comp.get("type", "NA")
            print(f"  {i}. {nombre} ({tipo})")

    def obtener_componente(self, indice: int):
        if 1 <= indice <= len(self.components):
            return self.components[indice - 1]
        return None
    
    def guardar_json(self):
        if not self.name:
            print("No hay datos para guardar")
            return
            
        nombre_archivo = input("Nombre del archivo (sin .json): ")
        if not nombre_archivo.strip():
            print("Nombre de archivo no puede estar vacío")
            return
            
        try:
            
            with open(f"{nombre_archivo}.json", 'w', encoding='utf-8') as file:
                json.dump(self, file, ensure_ascii=False, indent=4)
            print(f"Archivo guardado como {nombre_archivo}.json")
        
        except Exception as e:
            print(f"Error al guardar: {e}")