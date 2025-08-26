from rich.console import Console
from rich.prompt import Prompt
from Proceso import Proceso
from JsonHandler import JsonHandler

class Menu:
    def __init__(self):
        self.console = Console()
        self.procesoActual = None
        self.jsonHandler = JsonHandler()

    def __repr__(self) -> str:
        return f"Menu(console={self.console}, procesoActual={self.procesoActual})"
        
    def iniciar(self):
        while True:
            self.mostrar_menu_principal()
            opcion = self.pedir_opcion()
            
            if opcion == "1":
                self.console.print("Crear nuevo proceso")
                nombreProceso = input("Ingrese el nombre del proceso: ")
                self.procesoActual = Proceso(nombreProceso)


            elif opcion == "2":
                self.console.print("Cargar proceso wip")
                self.procesoActual = Proceso("cargando")
                success = self.jsonHandler.cargar_json(self.procesoActual)
                if success:
                    self.console.print("[blue]archivo cargado[/blue]")
                else:
                    self.console.print("[red]error al cargar el archivo[/red]")
            
            
            elif opcion == "3":
                self.console.print("Editar proceso wip")
            elif opcion == "4":
                self.console.print("Mostrar proceso")
                self.console.print(self.procesoActual)
            elif opcion == "5":
                self.console.print("Guardar proceso wip")
                if self.procesoActual is not None:
                    self.jsonHandler.guardar_json(self.procesoActual)
                else:
                    self.console.print("[red]No hay proceso actual para guardar.[/red]")
            elif opcion == "6":
                self.console.print("byeee")
                break
            else:
                self.console.print("Opción no válida")
            
            input("\nPresiona Enter para continuar...")
    
    def mostrar_menu_principal(self):
        self.console.clear()
        
        self.console.print("[bold italic blue]Bienvenido al simulador de procesos estocasticos[/bold italic blue]")

        opciones = [
            "1. Crear nuevo proceso",
            "2. Cargar proceso desde archivo",
            "3. Editar proceso actual",
            "4. Mostrar proceso",
            "5. Guardar proceso",
            "6. Salir"
        ]
        
        for opcion in opciones:
            self.console.print(f"  {opcion}")
        self.console.print("\n")
    
    def pedir_opcion(self) -> str:
        return Prompt.ask("Selecciona una opción", choices=["1", "2", "3", "4", "5", "6"])