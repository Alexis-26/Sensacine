"""Importacion de librerias"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Web_Scrapping.funciones_web_scrapping import *
from bs4 import BeautifulSoup

def Proceso():
    try:
        navegador = conexion()
        time.sleep(6)
        peliculas(navegador)
        time.sleep(6)
        top_películas(navegador)
        time.sleep(25)
        for i in range(1, 30):
            cant = len(bloques_peliculas(navegador))
            for pelicula in range(cant):
                lista_peliculas = bloques_peliculas(navegador)
                time.sleep(3)
                acceder_al_bloque(lista_peliculas[pelicula])
                time.sleep(10)
                btn_home(navegador)
                time.sleep(10)
                soup = bsoup(navegador)
                extraccion_informacion(soup)
                time.sleep(5)
                boton_regresar(navegador)
                time.sleep(5)
                boton_regresar(navegador)
                time.sleep(5)
            boton_siguiente(navegador)
            time.sleep(10)
        df = crear_dataframe()
        df.to_csv("Datasets/sensacine.csv")
    except Exception as e:
        df = crear_dataframe()
        df.to_csv("Datasets/sensacine.csv")
        print(e)

if __name__ == "__main__":
    Proceso()