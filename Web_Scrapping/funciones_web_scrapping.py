"""Archivo con las funciones para realizar el proceso Web Scrapping."""

"""Importamos las bibliotecas necesarias en este caso selenium y webdriver-manager"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

""""Se define la funcion para conectar con el navegador y pagina web"""
def conexion():

    """"Obtiene la ubicación del controlador de Chrome WebDriver e instala el controlador si es necesario"""
    driver = ChromeDriverManager().install()
    s = Service(driver)                                 #se crea un objeto Service utilizando la ubicacion del controlador
    opc = Options()                                     #se crea un objeto para configurar las opciones del navegador
    opc.add_argument("--window-size=1020,1200")         #se establece le tamaño de la ventana del navegador
    navegador = webdriver.Chrome(service=s, options=opc)#crea una instancia del navegador Chrome pasando el servicio y las opciones como argumentos
    navegador.get("https://www.sensacine.com")          #Abre la paguina web especificada
    time.sleep(10)                                      #se espera 10 seundos

    return navegador #retorna la clase navegador