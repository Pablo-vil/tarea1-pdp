from rich.console import Console
from rich.prompt import Prompt
from Proceso import Proceso

class Menu:
    def __init__(self):
        self.console = Console()
        
    def iniciar(self):
        while True:
            self.mostrar_menu_principal()
            opcion = self.pedir_opcion()
            
            if opcion == "1":
                self.console.print("Crear nuevo proceso")
                nombreProceso = input("Ingrese el nombre del proceso")
                Proceso(nombreProceso)

            elif opcion == "2":
                self.console.print("Cargar proceso (no implementado aún)")
            elif opcion == "3":
                self.console.print("Editar proceso (no implementado aún)")
            elif opcion == "4":
                self.console.print("Mostrar proceso (no implementado aún)")
            elif opcion == "5":
                self.console.print("Guardar proceso (no implementado aún)")
            elif opcion == "6":
                self.console.print("¡Adiós!")
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
            "\n"
        ]
        
        for opcion in opciones:
            self.console.print(f"  {opcion}")
        
    
    def pedir_opcion(self) -> str:
        return Prompt.ask("Selecciona una opción", choices=["1", "2", "3", "4", "5", "6"])