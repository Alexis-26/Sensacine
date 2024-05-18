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

#Función para el botón de Todas las películas
def todas_las_películas(navegador):
    #Se genera una variable para encontrar el botón de  todas las peliculas.
    botón = navegador.find_element(By.XPATH,"//*[@id='header-main-nav']/ul/li[1]/div/ul/li[7]/a") 
    #Aquí se ingresa al botón dándole click.
    botón.click()

#Función para el botón de Películas
def peliculas(navegador):                                                   #Crear el método para accionar el botón.
    btnpeliculas = navegador.find_element(By.CLASS_NAME, "header-nav-link") #Busqueda del botón películas y lo guarda en una variable llamada btnpeliculas.
    time.sleep(5)                                                           #Espera un tiempo para realizar la acción.
    btnpeliculas.click()                                                    #Realiza la accion de clikear sobre el boton películas.

#Código para cambiar de página

def boton_siguiente(navegador): #Se genera la función "boton_siguiente", con el parametro "navegador"

    pagina = navegador.find_element(By.CSS_SELECTOR, "a.xXx[href*='/peliculas/todas-peliculas/?page=']")  
    #La cadena de texto (CSS_SELECTOR) busca el enlace (a), que tenga como clase xXx, con atributo href el cual contiene la linea '/peliculas/todas-peliculas/?page='
    pagina.click() #Una vez encontrada la linea anterior, da click sobre ella y ejecuta el cambio de página

def boton_regresar(navegador):   #Se genera la función "boton_regresar", con el parámetro "navegador"
    navegador.back()             #Se creó una función para botón de regresar a la página del navegador,
                                 #usando back, al ejecutarlo, se regresa a la página anterior.