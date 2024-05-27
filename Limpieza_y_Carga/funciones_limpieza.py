import pandas as pd                     #Importamos la libreria de pandas

def sp_insert_puntaje(df:pd.DataFrame): #creamos un método en el que le damos como parámetro el dataframe
    df = df.where(pd.notna(df), None)   #permite que los Nan dentro de todo el dataframe cambien por None
    return df                           #retorna el dataframe con los datos Nan convertidos a None

def eliminar_espacios(df:pd.DataFrame):                                 #creamos un método en el que elimine los espacios y los \n de los títulos de las películas
    df["pelicula"] = df["pelicula"].str.replace("\n", "").str.strip()   #seleccionamos la columna a modificar y con .str.replace("\n","") elimina los espacios y \n de el título
    return df                                                           #retorna él dataframe limpio

def formato_fecha(df:pd.DataFrame):                                                                               #creamos un método en el que reciba como parámetro el dataframe y un diccionario que transforme un mes en su versión numero
    meses_dict = {                                                                                                #El diccionario que va a convertir el mes a su forma de número
    "enero": "01", "febrero": "02", "marzo": "03", "abril": "04", "mayo": "05", "junio": "06",
    "julio": "07", "agosto": "08", "septiembre": "09", "octubre": "10", "noviembre": "11", "diciembre": "12"
    }
    df["fecha_estreno"] = df["fecha_estreno"].str.replace("\n", "").str.strip()                                   #seleccionamos la columna a modificar y con .str.replace("\n","") elimina los espacios en blanco y los \n
    df["fecha_estreno"] = df["fecha_estreno"].str.replace("de","/").str.strip()                                   #seleccionamos la columna a modificar y con .str.replace("de","") elimina los espacios en blanco y los "de" que contiene la fecha
    df["fecha_estreno"] = df["fecha_estreno"].replace(meses_dict, regex=True)                                     #seleccionamos la columna a modificar y aplicamos el diccionario para que se reemplace con el numero del mes
    df["fecha_estreno"] = pd.to_datetime(df["fecha_estreno"], format="%d / %m / %Y")                              #seleccionamos la columna a modificar y la convertimos a tipo datetime
    return df                                                                                                     #retorna el dataframe modificado

def formato_presupuesto(df:pd.DataFrame):                                                           #creamos un metodo que reciba como parámetro un dataframe
    df["presupuesto"] = df["presupuesto"].str.replace(" USD", "").str.replace(" ", "").astype(int)  #seleccionamos la columna a modificar utilizando él .str.replace para que USD y espacios en blanco se eliminan y posteriormente cambie el dato a int
    return df                                                                                       #retorna el dataframe
