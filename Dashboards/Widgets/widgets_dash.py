import pandas as pd                                        #Importamos la librería de pandas
import dash                                                #Importamos la librería de Dash
import dash_bootstrap_components as dbc                    #Importamos los componentes de Bootstrap para Dash
from dash import Input, Output, dcc, html     

"""
Se realizó una función para la visualización de un botón desplegable,se despliega usuarios, 
medios y sensacine, predeterminando viaualizualmente Usuarios
se le agrega un id para llamarlo en el callback.
"""
def widgets_dropdown_dir():                                                     
    califdir = html.Div([                   
    dcc.Dropdown(["Usuarios", "Medios", "Sensacine"], "Usuarios", id="ddcalf",) 
    ])                                                                         
    return califdir
"""
Se realizó una función para poder visualizar un botón de rango,
sirve para agregar la cantidad de datos que se quieren ver en los dashboards.
"""
def widget_rslider(data:pd.DataFrame):                                         
    max_val= len(data)                                                         
    rango = dcc.RangeSlider(0, max_val,10, value=[0, 10], id="tcalf",
                            tooltip={"placement": "bottom", "always_visible": True})
    return rango

"""
La función creada realiza un widget donde despliega el total de presupuesto , promedio del presupuesto,
"minimo presupuesto", "maximo presupuesto", mostrando como valor pricipal a total de presupuesto 
y para poder identificar el botón se utiliza ddapresupuesto todo esto guardado en la variable 
cambio presupuesto.
"""
def widget_radio():
    Comparacion_prs = dcc.RadioItems(["Presupuesto total",
        "Presupuesto promedio"], id="radmpresupuesto", value="Presupuesto total", style={'color': '#000', 'font-size': "30px", 'background-color': "#e5b808", "margin-left":"20px",
                                                                                         "border-radius":"20px"})
    return Comparacion_prs

"""
Se creo una función dónde el widget  es de opción, este  selecciona uno 
de los botones  que esten en este seria presupuesto total y presupuesto promedio
se pone inline ya que este se cargar de poner los botones de manera horizontal.
"""
def widget_cambios():
    cambio_presupuesto = html.Div([
        dcc.Dropdown(["Total de presupuesto", "Promedio del presupuesto", "Minimo presupuesto", "Maximo presupuesto"],
                     "Total de presupuesto", id="ddapresupuesto")
    ])
    return cambio_presupuesto
"""
Se realizó una función para poder visualizar un botón de rango,
sirve para agregar el rango en años, que se se reflejará en los dashboards.
"""
def widget_rslider_tiempo(data:pd.DataFrame):
    min_val = data["año"].min()
    max_val = data["año"].max()

    year = dcc.RangeSlider(min_val, max_val, 1, marks=None, value=[2010, max_val],id="rtiempo",
                            tooltip={"placement": "bottom", "always_visible": True})
    return year



