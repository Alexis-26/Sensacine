"""Archivo con las funciones para realizar el proceso Web Scrapping."""

def peliculas(navegador):                                                   #Crear el método para accionar el botón.
    btnpeliculas = navegador.find_element(By.CLASS_NAME, "header-nav-link") #Busqueda del botón películas y lo guarda en una variable llamada btnpeliculas.
    time.sleep(5)                                                           #Espera un tiempo para realizar la acción.
    btnpeliculas.click()                                                    #Realiza la accion de clikear sobre el boton películas.