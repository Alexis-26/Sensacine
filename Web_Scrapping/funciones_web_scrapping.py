"""Archivo con las funciones para realizar el proceso Web Scrapping."""

"""Importamos las bibliotecas necesarias en este caso selenium y webdriver-manager"""
import time
import pandas as pd                                     #importar la librería para crear el dataframe
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
    opc.add_argument("--start-maximized")         #se establece le tamaño de la ventana del navegador
    navegador = webdriver.Chrome(service=s, options=opc)#crea una instancia del navegador Chrome pasando el servicio y las opciones como argumentos
    navegador.get("https://www.sensacine.com")          #Abre la paguina web especificada

    return navegador #retorna la clase navegador

#Función para el botón de Todas las películas
def top_películas(navegador):
    #Se genera una variable para encontrar el botón de  todas las peliculas.
    botón = navegador.find_element(By.LINK_TEXT,"Top películas") 
    #Aquí se ingresa al botón dándole click.
    botón.click()

#Función para el botón de Películas
def peliculas(navegador):                                                   #Crear el método para accionar el botón.
    btnpeliculas = navegador.find_element(By.CLASS_NAME, "header-nav-link") #Busqueda del botón películas y lo guarda en una variable llamada btnpeliculas.    
    btnpeliculas.click()                                                    #Realiza la accion de clikear sobre el boton películas.

#Código para cambiar de página
def boton_siguiente(navegador): #Se genera la función "boton_siguiente", con el parametro "navegador"
    pagina = navegador.find_element(By.CSS_SELECTOR, "a.xXx.button.button-md.button-primary-full.button-right")
    pagina.click() #Una vez encontrada la linea anterior, da click sobre ella y ejecuta el cambio de página

#Función para crear un dataframe 
def crear_dataframe(data:dict):             #Creación de un método que recibe como parámetro un diccionario
    dataframe = pd.DataFrame(data)          #Creacion de un dataframe a partir de un diccionario
    return dataframe                        #Retorna el dataframe

#Funcion para acceder al bloque de peliculas
def acceder_al_bloque(bloque):                                              #Crear el método para acceder al bloque de información de la película
    bloque_pelicula = bloque.find_element(By.TAG_NAME, "a")                 #Busqueda del boton por medio del nombre de la etiqueta.
    bloque_pelicula.click()                                                 #Da clic en el título de la película

#Funcion para presionar el boton de regresar del navegador web.    
def boton_regresar(navegador):   #Se genera la función "boton_regresar", con el parámetro "navegador"
    navegador.back()             #Se creó una función para botón de regresar a la página del navegador,
                                 #usando back, al ejecutarlo, se regresa a la página anterior.

#Funcion para obtener la lista de peliculas de una pagina.
def bloques_peliculas(navegador):
    bloques = navegador.find_element(By.CLASS_NAME, "gd-col-middle") # Busqueda por medio del nombre de la clase para ubicar donde se encuentran los demás elementos.
    lista_bloques = bloques.find_elements(By.CLASS_NAME, "mdl") # Busqueda por medio del nombre de la clase para obtener todos los elementos que coincidan con el nombre.
    return lista_bloques # Retorna la lista de elementos obtenidos.