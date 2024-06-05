import Limpieza_y_Carga.funciones_limpieza as fl
import pandas as pd
import Limpieza_y_Carga.funciones_carga_bd as fbd
from mysql.connector import connect, Error

def limpieza_datos():
    df = pd.read_csv("Dataset/sensacine.csv", index_col=0)
    df = fl.sp_insert_puntaje(df)
    df = fl.eliminar_espacios(df)
    df = fl.tipo_estreno(df)
    df = fl.eliminar_filas(df, "Acción", "fecha_estreno")
    df = fl.formato_fecha(df)
    df = fl.formato_presupuesto(df)
    df = fl.medios(df)
    df = fl.usuario(df)
    df = fl.sensacine(df)
    df = fl.fecha_produccion(df)
    df = fl.idioma_default(df)
    df.to_csv("Dataset/sensacine_limpio.csv", index=False)

def carga_datos():
    df = pd.read_csv("Dataset/sensacine_limpio.csv")
    db = fbd.connect_db()
    fbd.sp_insert_pelicula(db, df)
    fbd.sp_insert_director(db, df)
    fbd.sp_insert_estreno(db, df)
    fbd.sp_insert_genero(db, df)
    fbd.sp_insert_idioma(db, df)
    fbd.sp_insert_puntaje(db, df)
    fbd.sp_insert_especificaciones_tecnicas(db, df)
    fbd.sp_insert_director_pelicula(db, df)
    fbd.sp_insert_genero_pelicula(db, df)
    fbd.sp_insert_idioma_pelicula(db, df)
    fbd.sp_insert_detalle_pelicula(db, df)
    print("Listo los datos están cargados!")