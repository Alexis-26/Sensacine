#Importando las librerias necesarias.
import consultas_bd as cbd
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, dash_table, callback, Input, Output
import dash_bootstrap_components as dbc

"""Creando grafica de barras y retornando su id y la propiedad con la grafica."""
def grafica_barras(data:pd.DataFrame):
    bar = px.bar(data, x="director", y="promedio_usuarios", hover_name="director", color="promedio_usuarios")
    bar.update_layout(
        plot_bgcolor='#1b1a1a',
        paper_bgcolor='#1b1a1a',
        font_color='#faca0a'
    )
    return dcc.Graph(id="dash1bar", figure=bar)

"""Creando grafica de caja y retornando su id y la propiedad con la grafica."""
def grafica_caja(data:pd.DataFrame):
    box = px.box(data, x="promedio_usuarios")
    box.update_layout(
        plot_bgcolor='#1b1a1a',
        paper_bgcolor='#1b1a1a',
        font_color='#faca0a'
    )
    box.update_traces(marker=dict(color='#faca0a'))
    return dcc.Graph(id="dash1box", figure=box)

"""Creando grafica de scatter y retornando su id y la propiedad con la grafica."""
def grafica_scatter(data:pd.DataFrame):
    scatter = px.scatter(data, x="director", y="promedio_usuarios", color="promedio_usuarios",
                 hover_name="director")
    scatter.update_layout(
        plot_bgcolor='#1b1a1a',
        paper_bgcolor='#1b1a1a',
        font_color='#faca0a'
    )
    return dcc.Graph(id="dash1scatter", figure=scatter)

"""Creando la tabla con los datos utilizados y retornando su id con la propiedad data."""
def grafica_tabla(data:pd.DataFrame):
    tabla = dash_table.DataTable(id="dash1tabla", data= data.to_dict("records"), page_size=10)
    return tabla

"""
Recibiendo las entradas por medio de los widgets y procesando la salida por medio de las graficas.
Se realiza la funcion para actualizar los datos con relaccion a lo seleccionado por el usuario en los widgets.
"""
@callback(
    Output(component_id="dash1bar", component_property="figure"),
    Output(component_id="dash1box", component_property="figure"),
    Output(component_id="dash1scatter", component_property="figure"),
    Output(component_id="dash1tabla", component_property="data"),
    Input(component_id="ddcalf", component_property="value"),
    Input(component_id="rcalf", component_property="value")
)

def evento(opcion, rango):
    conexionbd = cbd.connect_db()
    df = cbd.df_director_calificaciones(conexionbd)
    data = None
    
    if opcion == "Usuarios":
        data = "promedio_usuarios"
    elif opcion == "Medios":
        data = "promedio_medios"
    elif opcion == "Sensacine":
        data = "promedio_sensacine"

    min_val, max_val = rango
    df = df.iloc[min_val:max_val]
    bar = px.bar(df, x="director", y=data, hover_name="director", color=data)
    bar.update_layout(
        plot_bgcolor='#1b1a1a',
        paper_bgcolor='#1b1a1a',
        font_color='#faca0a'
    )
    box = px.box(df, x=data)
    box.update_layout(
        plot_bgcolor='#1b1a1a',
        paper_bgcolor='#1b1a1a',
        font_color='#faca0a'
    )
    box.update_traces(marker=dict(color='#faca0a'))
    scatter = px.scatter(df, x="director", y=data, color=data,
                 hover_name="director")
    scatter.update_layout(
        plot_bgcolor='#1b1a1a',
        paper_bgcolor='#1b1a1a',
        font_color='#faca0a'
    )
    tabla = df.to_dict("records")
    return bar, box, scatter, tabla
