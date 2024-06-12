#Importando las librerias necesarias.
import consultas_bd as cbd
import pandas as pd
import plotly.express as px
from dash import dcc, dash_table, callback, Input, Output

"""Creando grafica de lineas y retornando su id y la propiedad con la grafica."""
def grafica_lineas(data:pd.DataFrame):
    line = px.line(data, x="año", y="total_presupuesto")
    line.update_layout(
        plot_bgcolor='#1b1a1a',
        paper_bgcolor='#1b1a1a',
        font_color='#faca0a'
    )
    line.update_traces(marker=dict(color='#faca0a'))
    return dcc.Graph(id="dash3line", figure=line)

"""Creando grafica de histograma y retornando su id y la propiedad con la grafica."""
def grafica_histograma(data:pd.DataFrame):
    hist = px.histogram(data,  x="año")
    hist.update_layout(
        plot_bgcolor='#1b1a1a',
        paper_bgcolor='#1b1a1a',
        font_color='#faca0a'
    )
    hist.update_traces(marker=dict(color='#faca0a'))
    return dcc.Graph(id="dash3histograma", figure=hist)

"""Creando grafica de barras y retornando su id y la propiedad con la grafica."""
def grafica_barras(data:pd.DataFrame):
    bar = px.bar(data, x="año", y="total_presupuesto")
    bar.update_layout(
        plot_bgcolor='#1b1a1a',
        paper_bgcolor='#1b1a1a',
        font_color='#faca0a'
    )
    bar.update_traces(marker=dict(color='#faca0a'))
    return dcc.Graph(id="dash3bar", figure=bar)

"""Creando la tabla con los datos utilizados y retornando su id con la propiedad data."""
def grafica_tabla(data:pd.DataFrame):
    tabla = dash_table.DataTable(id="dash3tabla", data= data.to_dict("records"), page_size=10)
    return tabla

"""
Recibiendo las entradas por medio de los widgets y procesando la salida por medio de las graficas.
Se realiza la funcion para actualizar los datos con relaccion a lo seleccionado por el usuario en los widgets.
"""
@callback(
    Output(component_id="dash3line", component_property="figure"),
    Output(component_id="dash3histograma", component_property="figure"),
    Output(component_id="dash3bar", component_property="figure"),
    Output(component_id="dash3tabla", component_property="data"),
    Input(component_id="ddapresupuesto", component_property="value"),
    Input(component_id="rtiempo", component_property="value")
)
def evento(opcion, rango):
    conexionbd = cbd.connect_db()
    df = cbd.df_presupuesto_fecha(conexionbd)
    data = None

    if opcion == "Total de presupuesto":
        data = "total_presupuesto"
    elif opcion == "Promedio del presupuesto":
        data = "promedio_presupuesto"
    elif opcion == "Minimo presupuesto":
        data = "min_presupuesto"
    elif opcion == "Maximo presupuesto":
        data = "max_presupuesto"

    min_val, max_val = rango
    df_filtrado = df[(df["año"] >= min_val) & (df["año"] <= max_val)]
    line = px.line(df_filtrado, x="año", y=data)
    line.update_layout(
        plot_bgcolor='#1b1a1a',
        paper_bgcolor='#1b1a1a',
        font_color='#faca0a'
    )
    line.update_traces(marker=dict(color='#faca0a'))
    hist = px.histogram(df_filtrado, x="año", y=data)
    hist.update_layout(
        plot_bgcolor='#1b1a1a',
        paper_bgcolor='#1b1a1a',
        font_color='#faca0a'
    )
    hist.update_traces(marker=dict(color='#faca0a'))
    bar = px.bar(df, x="año", y=data)
    bar.update_layout(
        plot_bgcolor='#1b1a1a',
        paper_bgcolor='#1b1a1a',
        font_color='#faca0a'
    )
    bar.update_traces(marker=dict(color='#faca0a'))
    tabla = df_filtrado.to_dict("records")
    return line, hist, bar, tabla