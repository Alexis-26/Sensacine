"""Archivo con las funciones para realizar el proceso Web Scrapping."""
#Función para el botón de Todas las películas
def todas_las_películas(navegador):
    #Se genera una variable para encontrar el botón de  todas las peliculas.
    botón = navegador.find_element(By.XPATH,"//*[@id='header-main-nav']/ul/li[1]/div/ul/li[7]/a") 
    #Aquí se ingresa al botón dándole click.
    botón.click()