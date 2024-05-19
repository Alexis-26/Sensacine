"""Se crea un archivo, en el cual se desarrollará el proceso de Web Scrapping."""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Web_Scrapping.funciones_web_scrapping import *

def Proceso():
    navegador = conexion()
    time.sleep(5)
    peliculas(navegador)
    time.sleep(5)
    top_películas(navegador)
    time.sleep(5)
    for i in range(2):
        acceder_al_bloque(navegador)
        time.sleep(10)
        boton_regresar(navegador)
        time.sleep(10)
        boton_siguiente(navegador)
        time.sleep(8)
    

if __name__ == "__main__":
    Proceso()


