#Importando las librerias necesarias.
import pandas as pd
import plotly.express as px
from dash import dcc, dash_table, callback, Input, Output

df_org = None

"""Creando grafica de barras y retornando su id y la propiedad con la grafica."""
def grafica_barras(data:pd.DataFrame):
    global df_org
    df_org = data
    data = data[data["total_presupuesto"] != 0]
    bar = px.bar(data, x="distribuidora", y="total_presupuesto")
    bar.update_layout(
        plot_bgcolor="#2B2A2A",
        paper_bgcolor="#2B2A2A",
        font_color="#ffffff"
    )
    bar.update_traces(marker=dict(color="#faca0a"))
    return dcc.Graph(id="dash2bar", figure=bar)

"""Creando grafica de pastel y retornando su id y la propiedad con la grafica."""
def grafica_pastel(data:pd.DataFrame):
    df_pastel = data[data["total_presupuesto"] != 0]
    total_presupuesto = df_pastel["total_presupuesto"].sum()
    df_pastel["porcentaje"] = df_pastel["total_presupuesto"] / total_presupuesto
    df_pastel.loc[df_pastel["porcentaje"] < 0.05, "distribuidora"] = "Otros"
    pastel = px.pie(df_pastel, names="distribuidora", values="total_presupuesto")
    pastel.update_layout(
        plot_bgcolor="#2B2A2A",
        paper_bgcolor="#2B2A2A",
        font_color="#ffffff"
    )
    return dcc.Graph(id="dash2pastel", figure=pastel)

"""Creando grafica de scatter y retornando su id y la propiedad con la grafica."""
def grafica_scatter(data:pd.DataFrame):
    global df_org
    df_org = data
    scatter = px.scatter(data, x="distribuidora", y="total_presupuesto")
    scatter.update_layout(
        plot_bgcolor="#2B2A2A",
        paper_bgcolor="#2B2A2A",
        font_color="#ffffff"
    )
    scatter.update_traces(marker=dict(size=15, color="#faca0a"))
    return dcc.Graph(id="dash2scatter", figure=scatter)

"""Creando la tabla con los datos utilizados y retornando su id con la propiedad data."""
def grafica_tabla(data:pd.DataFrame):
    global df_org
    df_org = data
    tabla = dash_table.DataTable(id="dash2tabla", data= data.to_dict("records"), page_size=10, style_table={"overflowX": "auto", "width": "100%", "minWidth": "100%"},
        style_cell={"textAlign": "left", "whiteSpace": "normal", "height": "auto"},
        style_header={"backgroundColor": "#e5b808", "color": "#2B2A2A"},
        style_data={"backgroundColor": "rgb(50, 50, 50)", "color": "white"})
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
    df = df_org
    data = None

    if opcion == "Presupuesto total":
        data = "total_presupuesto"
    elif opcion == "Presupuesto promedio":
        data = "promedio_presupuesto"

    df = df[df[data] != 0]
    bar = px.bar(df, x="distribuidora", y=data)
    bar.update_layout(
        plot_bgcolor="#2B2A2A",
        paper_bgcolor="#2B2A2A",
        font_color="#ffffff"
    )
    bar.update_traces(marker=dict(color="#faca0a"))
    scatter = px.scatter(df, x="distribuidora", y=data)
    scatter.update_layout(
        plot_bgcolor="#2B2A2A",
        paper_bgcolor="#2B2A2A",
        font_color="#ffffff"
    )
    scatter.update_traces(marker=dict(size=15, color="#faca0a"))
    # Realizando calculos para modificar la grafica de pastel
    df_pastel = df
    presupuesto = df_pastel[data].sum()
    df_pastel["porcentaje"] = df_pastel[data] / presupuesto
    df_pastel.loc[df_pastel["porcentaje"] < 0.05, "distribuidora"] = "Otros"
    pastel = px.pie(df_pastel, names="distribuidora", values=data)
    pastel.update_layout(
        plot_bgcolor="#2B2A2A",
        paper_bgcolor="#2B2A2A",
        font_color="#ffffff"
    )
    return bar, pastel, scatter