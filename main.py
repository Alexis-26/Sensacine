"""Archivo main para incializar el proyecto."""
"""Importando las funciones."""
import Proceso_Web_Scrapping as pwb
import proceso_limpieza_y_carga as plc
from Pagina_principal import app

"""Menu de opciones para ejecutar cada proceso."""
def mostrar_menu():
    print("Menú de selección de procesos:")
    print("1. Web Scrapping")
    print("2. Limpieza y Carga de datos")
    print("3. Dashboards")
    print("4. Salir")

"""Ejecutando el menu para revisar cada proceso."""
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            pwb.web_scrapping()
        elif opcion == "2":
            plc.limpieza_datos()
            plc.carga_datos()
        elif opcion == "3":
            app.run_server()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("No existe esta opción!")

if __name__ == "__main__":
    main()