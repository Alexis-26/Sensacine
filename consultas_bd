import pandas as pd
from mysql.connector import Error
import mysql.connector

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

def transformar_df(conexionDB,query):
    cursor = conexionDB.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [i[0] for i in cursor.description] # Obtén los nombres de las columnas
    cursor.close()
    df = pd.DataFrame(rows, columns=columns)
    return df

"""se realizara un dataframe extraido de la base de datos donde muestre directores y calificaciones"""
def df_director_calificaciones(conexiondb):
    query = ("select d.nombre as director, "
             "count(p.id_puntaje) as cantidad_calificaciones, "
             "avg(p.usuarios) as promedio_usuarios, "
             "avg(p.medios) as promedio_medios, "
             "avg(p.sensacine) as promedio_sensacine "
             "from director d "
             "join director_pelicula dp on d.id_director = dp.id_director "
             "join detalle_pelicula det on dp.id_directorp = det.id_directorp "
             "join puntaje p on det.id_pelicula = p.id_pelicula "
             "group by d.nombre "
             "order by promedio_usuarios desc, cantidad_calificaciones desc;")
    direc_calificaciones = transformar_df(conexiondb, query)
    direc_calificaciones['promedio_usuarios'] = direc_calificaciones['promedio_usuarios'].astype(float)     #se combierten los datos a tipo float para evitar errores
    direc_calificaciones['promedio_medios'] = direc_calificaciones['promedio_medios'].astype(float)
    direc_calificaciones['promedio_sensacine'] = direc_calificaciones['promedio_sensacine'].astype(float)
    return direc_calificaciones

"""se realizara un dataframe extraido de la base de datos donde muestre presupuestos de las distrubuidoras"""
def df_presupuestos_distribuidoras(conexiondb):
    query = ("select e.distribuidora, "
             "count(e.id_pelicula) as cantidad_peliculas, "
             "sum(e.presupuestos) as total_presupuesto, "
             "avg(e.presupuestos) as promedio_presupuesto "
             "from especificaciones_tecnicas e "
             "where e.distribuidora is not null "
             "group by e.distribuidora;")
    presupuestos = transformar_df(conexiondb, query)
    presupuestos["total_presupuesto"]=presupuestos["total_presupuesto"].astype(float)
    presupuestos["promedio_presupuesto"]=presupuestos["promedio_presupuesto"].astype(float)
    return presupuestos

"""se realizara un dataframe extraido de la base de datos donde muestre presupuesto a con base a los años"""
def df_presupuesto_fecha(conexiondb):
    query = ("select year(e.año_produccion) as año, "
             "count(e.id_pelicula) as cantidad_peliculas, "
             "sum(e.presupuestos) as total_presupuesto, "
             "avg(e.presupuestos) as promedio_presupuesto, "
             "min(e.presupuestos) as min_presupuesto, "
             "max(e.presupuestos) as max_presupuesto "
             "from especificaciones_tecnicas e "
             "where e.presupuestos > 0 "
             "group by year(e.año_produccion) "
             "order by year(e.año_produccion);")
    presupuesto_fecha = transformar_df(conexiondb, query)
    presupuesto_fecha["total_presupuesto"]=presupuesto_fecha["total_presupuesto"].astype(float)
    presupuesto_fecha["promedio_presupuesto"]=presupuesto_fecha["promedio_presupuesto"].astype(float)
    presupuesto_fecha["min_presupuesto"]=presupuesto_fecha["min_presupuesto"].astype(float)
    presupuesto_fecha["max_presupuesto"]=presupuesto_fecha["max_presupuesto"].astype(float)
    return presupuesto_fecha