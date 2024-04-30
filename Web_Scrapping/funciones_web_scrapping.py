"""Archivo con las funciones para realizar el proceso Web Scrapping."""

#Funcion para obtener los servicios y se estructure el navegador, retornando el navegador con la pagina web

#Se importan las librerias necesarias
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Definir la funcion para conectarse al navegador y visitar una paguina web
def conexion():
    driver = ChromeDriverManager().install() #se usa para instalar el controlador de chrome
    s = Service(driver) #crea un objeto servicio 

    #Se configura las opciones de navegador
    opc = Options()
    opc.add_argument("--window-size= 1020, 1200")

    navegador = webdriver.Chrome(service=s, options=opc) #se crea una instancia del navegador chrome
    navegador.get("https://www.sensacine.com") #se abre la pagina web especificada
    time.sleep(5) #Se hace una espera de 5 segundos

conexion()