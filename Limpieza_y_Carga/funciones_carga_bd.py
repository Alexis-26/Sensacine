import pandas as pd
from mysql.connector import Error
import mysql.connector
import numpy as np

def connect_db():
        try:
            # Establecer la conexión con la base de datos
            conexionDB = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="26097278",
                database="sensacine"
            )
            return conexionDB
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")

def sp_insert_pelicula(conexionDB, df):         #creacion de la funcion de insercion de datos pelicula
    cursor = conexionDB.cursor()
    for index, row in df.iterrows():
        nombre = row['pelicula']
        sql = "CALL sp_insert_pelicula(%s)"
        cursor.execute(sql, (nombre,))
    print("Se incertaron datos en pelicula")
    conexionDB.commit()

def sp_insert_director(conexionDB, df):         #creacion de la funcion de insercion de datos director
    cursor = conexionDB.cursor()
    for index, row in df.iterrows():
        director = row['director']
        sql = "CALL sp_insert_director(%s)"
        cursor.execute(sql, (director,))
    print("Se incertaron datos en director")
    conexionDB.commit()

def sp_insert_estreno(conexionDB, df):          #creacion de la funcion de insercion de datos estreno
    cursor = conexionDB.cursor()
    peliculas_unicas = df.drop_duplicates(subset=['pelicula'])
    for index, row in peliculas_unicas.iterrows():
        tipo_estreno = row['tipo_estreno']
        sql = "CALL sp_insert_estreno(%s)"
        cursor.execute(sql, (tipo_estreno,))
    print("Se incertaron datos en estreno")
    conexionDB.commit()

def sp_insert_genero(conexionDB, df):           #creacion de la funcion de insercion de datos genero
    cursor = conexionDB.cursor()
    for index, row in df.iterrows():
        genero = row['genero']
        sql = "CALL sp_insert_genero(%s)"
        cursor.execute(sql, (genero,))
    print("Se incertaron datos en genero")
    conexionDB.commit()

def sp_insert_idioma(conexionDB, df):           #creacion de la funcion de insercion de datos idioma
    cursor = conexionDB.cursor()
    for index, row in df.iterrows():
        idioma = row['idioma']
        sql = "CALL sp_insert_idioma(%s)"
        cursor.execute(sql, (idioma,))
    print("Se incertaron datos en idioma")
    conexionDB.commit()

def sp_insert_puntaje(conexionDB, df):          #creacion de la funcion de insercion de datos puntaje
    cursor = conexionDB.cursor()
    df = df.replace({np.nan: None})
    for index, row in df.iterrows():
        medios = row['calf_medios']
        usuarios = row['calf_usuarios']
        sensacine = row['calf_sensacine']
        pelicula = row['pelicula']
        sql = "CALL sp_insert_puntaje(%s, %s, %s, %s)"
        cursor.execute(sql, (medios, usuarios, sensacine, pelicula))
    print("Se incertaron datos en puntaje")
    conexionDB.commit()

def sp_insert_especificaciones_tecnicas(conexionDB, df):        #creacion de la funcion de insercion de datos tecnicas
    cursor = conexionDB.cursor()
    df = df.replace({np.nan: None})
    for index, row in df.iterrows():
        nacionalidad = row['nacionalidad']
        distribuidora = row['distribuidora']
        presupuestos = row['presupuesto']
        fecha_produccion = row['fecha_produccion']
        nombre_pelicula = row['pelicula']
        sql = "CALL sp_insert_especificaciones_tecnicas(%s, %s, %s, %s, %s)"
        cursor.execute(sql, (nacionalidad, distribuidora, presupuestos, fecha_produccion, nombre_pelicula))
    print("Se incertaron datos en especificaciones_tecnicas")
    conexionDB.commit()

def sp_insert_director_pelicula(conexionDB, df):                #creacion de la funcion de insercion de datos director_pelicula
    cursor = conexionDB.cursor()
    for index, row in df.iterrows():
        nombre_director = row['director'].strip()
        pelicula = row['pelicula'].strip()
        sql = "CALL sp_insert_director_pelicula(%s, %s)"
        cursor.execute(sql, (nombre_director, pelicula))
    print("Se incertaron datos en director_pelicula")
    conexionDB.commit()

def sp_insert_genero_pelicula(conexionDB, df):                  #creacion de la funcion de insercion de datos en genero_pelicula
    cursor = conexionDB.cursor()
    for index, row in df.iterrows():
        id_genero = row['genero'].strip()
        pelicula = row['pelicula'].strip()
        sql = "CALL sp_insert_genero_pelicula(%s, %s)"
        cursor.execute(sql, (id_genero, pelicula))
    print("Se incertaron datos en genero_pelicula")
    conexionDB.commit()

def sp_insert_idioma_pelicula(conexionDB, df):                 #creacion de la funcion de insercion de datos en idioma_pelicula
    cursor = conexionDB.cursor()
    for index, row in df.iterrows():
        idioma = row['idioma'].strip()
        pelicula = row['pelicula'].strip()
        sql = "CALL sp_insert_idioma_pelicula(%s, %s)"
        cursor.execute(sql, (idioma, pelicula))
    print("Se incertaron datos en idioma_pelicula")
    conexionDB.commit()

def sp_insert_detalle_pelicula(conexionDB, df):                 #creacion de la funcion de insercion de datos en detalle_pelicula
    cursor = conexionDB.cursor()
    df_no_duplicada = df.drop_duplicates(subset=['pelicula'])
    for index, row in df_no_duplicada.iterrows():
        duracion_insertar = row['duracion']
        pelicula = row['pelicula'].strip()
        fecha = row["fecha_estreno"]
        sql = "CALL sp_insert_detalle_pelicula(%s, %s, %s)"
        cursor.execute(sql, (pelicula, duracion_insertar, fecha))
    print("Se incertaron datos en detalle_pelicula")
    conexionDB.commit()