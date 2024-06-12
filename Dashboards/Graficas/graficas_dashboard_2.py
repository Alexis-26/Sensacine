#Importando las librerias necesarias.
import consultas_bd as cbd
import pandas as pd
import plotly.express as px
from dash import dcc, dash_table, callback, Input, Output

"""Creando grafica de barras y retornando su id y la propiedad con la grafica."""
def grafica_barras(data:pd.DataFrame):
    data = data[data["total_presupuesto"] != 0]
    bar = px.bar(data, x="distribuidora", y="total_presupuesto")
    bar.update_layout(
        plot_bgcolor='#1b1a1a',
        paper_bgcolor='#1b1a1a',
        font_color='#faca0a'
    )
    bar.update_traces(marker=dict(color='#faca0a'))
    return dcc.Graph(id="dash2bar", figure=bar)

"""Creando grafica de pastel y retornando su id y la propiedad con la grafica."""
def grafica_pastel(data:pd.DataFrame):
    df = data[data["total_presupuesto"] != 0]
    total_presupuesto = df["total_presupuesto"].sum()
    df["porcentaje"] = df["total_presupuesto"] / total_presupuesto
    df.loc[df["porcentaje"] < 0.05, "distribuidora"] = "Otros"
    pastel = px.pie(df, names="distribuidora", values="total_presupuesto")
    pastel.update_layout(
        plot_bgcolor='#1b1a1a',
        paper_bgcolor='#1b1a1a',
        font_color='#faca0a'
    )
    return dcc.Graph(id="dash2pastel", figure=pastel)

"""Creando grafica de scatter y retornando su id y la propiedad con la grafica."""
def grafica_scatter(data:pd.DataFrame):
    scatter = px.scatter(data, x="distribuidora", y="total_presupuesto", color="total_presupuesto",
                 hover_name="distribuidora")
    scatter.update_layout(
        plot_bgcolor='#1b1a1a',
        paper_bgcolor='#1b1a1a',
        font_color='#faca0a'
    )
    return dcc.Graph(id="dash2scatter", figure=scatter)

"""Creando la tabla con los datos utilizados y retornando su id con la propiedad data."""
def grafica_tabla(data:pd.DataFrame):
    tabla = dash_table.DataTable(id="dash2tabla", data= data.to_dict("records"), page_size=10)
    return tabla

"""
Recibiendo las entradas por medio de los widgets y procesando la salida por medio de las graficas.
Se realiza la funcion para actualizar los datos con relaccion a lo seleccionado por el usuario en los widgets.
"""
@callback(
    Output(component_id="dash2bar", component_property="figure"),
    Output(component_id="dash2pastel", component_property="figure"),
    Output(component_id="dash2scatter", component_property="figure"),
    Input(component_id="radmpresupuesto", component_property="value")
)

def evento(opcion):
    conexionbd = cbd.connect_db()
    df = cbd.df_presupuestos_distribuidoras(conexionbd)
    df2 = df
    data = None

    if opcion == "Presupuesto total":
        data = "total_presupuesto"
    elif opcion == "Presupuesto promedio":
        data = "promedio_presupuesto"

    df = df[df[data] != 0]
    bar = px.bar(df, x="distribuidora", y=data)
    bar.update_layout(
        plot_bgcolor='#1b1a1a',
        paper_bgcolor='#1b1a1a',
        font_color='#faca0a'
    )
    bar.update_traces(marker=dict(color='#faca0a'))
    scatter = px.scatter(df, x="distribuidora", y=data, color=data,
                 hover_name="distribuidora")
    scatter.update_layout(
        plot_bgcolor='#1b1a1a',
        paper_bgcolor='#1b1a1a',
        font_color='#faca0a'
    )
    
    # Realizando calculos para modificar la grafica de pastel
    presupuesto = df2[data].sum()
    df2["porcentaje"] = df2[data] / presupuesto
    df2.loc[df2["porcentaje"] < 0.05, "distribuidora"] = "Otros"
    pastel = px.pie(df2, names="distribuidora", values=data)
    pastel.update_layout(
        plot_bgcolor='#1b1a1a',
        paper_bgcolor='#1b1a1a',
        font_color='#faca0a'
    )
    return bar, pastel, scatter