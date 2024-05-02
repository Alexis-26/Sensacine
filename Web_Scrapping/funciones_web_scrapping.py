
#Código para cambiar de página

def boton_siguiente(navegador): #Se genera la función "boton_siguiente", con el parametro "navegador"

    pagina = navegador.find_element(By.CSS_SELECTOR, "a.xXx[href*='/peliculas/todas-peliculas/?page=']")  
    #La cadena de texto (CSS_SELECTOR) busca el enlace (a), que tenga como clase xXx, con atributo href el cual contiene la linea '/peliculas/todas-peliculas/?page='
    pagina.click() #Una vez encontrada la linea anterior, da click sobre ella y ejecuta el cambio de página