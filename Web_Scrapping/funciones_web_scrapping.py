"""Archivo con las funciones para realizar el proceso Web Scrapping."""

"""Importamos las bibliotecas necesarias en este caso selenium y webdriver-manager"""
import time
import pandas as pd                                     #importar la librería para crear el dataframe
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

"""Diccionario para almacenar los datos en un dataframe. Esta estructurado segun el nombre de la columna correspondiente a la informacion."""
datos = {
        "pelicula":[],
        "fecha_estreno":[],
        "tipo_estreno":[],
        "duracion":[],
        "genero":[],
        "director":[],
        "calf_medios":[],
        "calf_usuarios":[],
        "calf_sensacine":[],
        "nacionalidad":[],
        "distribuidora":[],
        "fecha_produccion":[],
        "presupuesto":[],
        "idioma":[]
    }

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
def crear_dataframe(): #Creación de un método para generar un dataframe
    dataframe = pd.DataFrame(datos) #Creacion de un dataframe a partir del diccionario "datos"
    dataframe = dataframe.explode("genero").explode("director").explode("idioma") #Modifica el dataframe en el diccionario para ampliar las columnas con datos multiples.
    return dataframe #Retorna el dataframe

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

#Funcion para presionar el boton que se encuentra dentro de cada pelicula
def btn_home(navegador):
    btn = navegador.find_element(By.CSS_SELECTOR, "#roller-1 > div.roller-overflow > div > a.xXx.home.roller-item") #Busqueda del boton.
    btn.click() #Accionando el boton.

#Funcion para construir el bs4
def bsoup(navegador):
    soup = BeautifulSoup(navegador.page_source, "html5lib") #Recolectando el codigo html de la pagina donde se encuentra la informacion a recabar.
    return soup #Retorna el codigo de la pagina para posteriormente realizar busquedas.


#Funcion para extraer la información de las peliculas.
def extraccion_informacion(soup:BeautifulSoup):
    temp_datos = {
        "pelicula":[],
        "fecha_estreno":[],
        "tipo_estreno":[],
        "duracion":[],
        "genero":[],
        "director":[],
        "calf_medios":[],
        "calf_usuarios":[],
        "calf_sensacine":[],
        "nacionalidad":[],
        "distribuidora":[],
        "fecha_produccion":[],
        "presupuesto":[],
        "idioma":[]
    }

    """Realizando busquedas de la informacion general, utilizando las funciones de soup (find, findAll).
    Dentro de cada funcion se realizo la busque con etiquetas de html y el nombre de las clases."""

    info_general = soup.find("div", attrs={"class":"meta-body"}) #Aqui inicia con el uso del codigo html de la pagina que fue obtenido en la funcion "bsoup".
    meta_datos = info_general.find("div", attrs={"class":"meta-body-item meta-body-info"})
    
    fecha_estreno = meta_datos.find("a")
    tipo_estreno = meta_datos.find("span", attrs={"class":"meta-release-type"})
    genero = meta_datos.findAll("a", attrs={"class":"xXx"})

    info_director = info_general.find("div", attrs={"class":"meta-body-item meta-body-direction meta-body-oneline"})
    director = info_director.findAll("a", attrs={"class":"xXx dark-grey-link"})

    """Realizando proceso de eliminacion de elementos html provenientes del la recoleccion de datos."""
    pelicula = info_general.findAll("div", attrs={"class":"meta-body-item"})[-1]
    span = pelicula.find("span")
    span.extract()
    
    """Realizando proceso de eliminacion de elementos html provenientes del la recoleccion de datos."""
    duracion = info_general.find("div", attrs={"class":"meta-body-item meta-body-info"})
    span_1 = duracion.find("span")
    a = duracion.find("a")
    span_1.extract()
    a.extract()

    """Guardado de la informacion en el diccionario "datos". """
    temp_datos["pelicula"].append(pelicula.text)
    temp_datos["fecha_estreno"].append(fecha_estreno.text)
    temp_datos["tipo_estreno"].append(tipo_estreno.text)
    temp_datos["duracion"].append(duracion.text[5:13])

    """Guardado de la informacion en el diccionario "datos". """
    lista_genero = []
    cant_genero = len(genero)
    for i in range(1, cant_genero): #Se utiliza un ciclo porque el dato puede ser multiple.
        lista_genero.append(genero[i].text)
    temp_datos["genero"].append(lista_genero)
    
    """Guardado de la informacion en el diccionario "datos". """
    lista_director = []
    cant_director = len(director)
    for i in range(cant_director): #Se utiliza un ciclo porque el dato puede ser multiple.
        lista_director.append(director[i].text)
    temp_datos["director"].append(lista_director)

    """Realizando la busqueda de la informacion de los rankings."""
    bloques_rankings = soup.findAll("div", attrs={"class":"rating-item"}) #Aqui inicia con el uso del codigo html de la pagina que fue obtenido en la funcion "bsoup".
    cant_bloques = len(bloques_rankings)

    for i in range(cant_bloques):
        info_bloque = bloques_rankings[i].find("div", attrs={"class":"rating-item-content"})
        titulo_bloque = info_bloque.find("a", attrs={"class":"xXx rating-title"})
        if titulo_bloque is not None: #Validando los objetos
            titulo = titulo_bloque.text

            """Guardando la informacion en el diccionario"""
            if titulo == " Medios ":
                info_estrellas = info_bloque.find("div", attrs={"class":"stareval stareval-small stareval-theme-default"})
                estrellas = info_estrellas.find("span", attrs ={"class":"stareval-note"})
                temp_datos["calf_medios"].append(estrellas.text)
            if titulo == " Usuarios ":
                info_estrellas = info_bloque.find("div", attrs={"class":"stareval stareval-small stareval-theme-default"})
                estrellas = info_estrellas.find("span", attrs ={"class":"stareval-note"})
                temp_datos["calf_usuarios"].append(estrellas.text)
            if titulo == "Sensacine":
                info_estrellas = info_bloque.find("div", attrs={"class":"stareval stareval-small stareval-theme-default"})
                estrellas = info_estrellas.find("span", attrs ={"class":"stareval-note"})
                temp_datos["calf_sensacine"].append(estrellas.text)

    """Realizando la busqueda de la informacion de las especificaciones tecnicas"""
    info_tecnica = soup.find("section", attrs={"class":"section ovw ovw-technical"}) #Aqui inicia con el uso del codigo html de la pagina que fue obtenido en la funcion "bsoup".
    renglones_info = info_tecnica.findAll("div", attrs={"class":"item"})

    info_nacionalidad = renglones_info[0]
    nacionalidad = info_nacionalidad.find("a", attrs={"class":"xXx nationality"})

    info_distribuidora = renglones_info[1]
    distribuidora = info_distribuidora.find("a", attrs={"class":"xXx that blue-link"})

    info_fecha_produccion = renglones_info[2]
    fecha_produccion = info_fecha_produccion.find("span", attrs={"class":"that"})

    info_presupuesto = renglones_info[5]
    presupuesto = info_presupuesto.find("span", attrs={"class":"that"})
    
    info_idioma = renglones_info[7]
    idioma = info_idioma.find("span", attrs={"class":"that"})

    """Realizando proceso de eliminacion de elementos html provenientes del la recoleccion de datos."""
    idioma_text = idioma.text.strip()
    lista_idioma_pre = idioma_text.split(",")

    """Guardado de la informacion en el diccionario "datos". """
    lista_idioma = []
    for i in lista_idioma_pre: #Se utiliza un ciclo porque el dato puede ser multiple.
        lista_idioma.append(i.strip())
    temp_datos["idioma"].append(lista_idioma)

    """Guardado de la informacion en el diccionario "datos". """
    if nacionalidad is not None:
        temp_datos["nacionalidad"].append(nacionalidad.text)

    if distribuidora is not None:
        temp_datos["distribuidora"].append(distribuidora.text)
    
    if fecha_produccion is not None:
        temp_datos["fecha_produccion"].append(fecha_produccion.text)

    if presupuesto is not None:
        temp_datos["presupuesto"].append(presupuesto.text)

    for key, value in temp_datos.items(): # Valiacion para las listas vacias, en caso de estar vacias se interta tipo nulo.
        if value == []:
            temp_datos[key].append(None)

    for key in temp_datos:
        datos[key].extend(temp_datos[key]) #Guardando toda la informacion en el diccionario "datos"