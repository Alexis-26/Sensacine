
def widgets_dropdown_dir():                                                     #Se realizó una función para la visualización de un botón desplegable
    califdir = html.Div([                   
    dcc.Dropdown(["Usuarios", "Medios", "Sensacine"], "Usuarios", id="tcalf",) #Se despliega usuarios, medios y sensacine, predeterminando viaualizualmente Usuarios
    ])                                                                         #Se le agrega un id para llamarlo en el callback
    return califdir

def widget_rslider(data:pd.DataFrame):                                          #Se realizó una función para poder visualizar un botón de rango
    max_val= len(data)                                                          #Sirve para agregar la cantidad de datos que se quieren ver en los dashboards.
    rango = dcc.RangeSlider(1, max_val,10, value=[0, 10], id="ddcalf",
                            tooltip={"placement": "bottom", "always_visible": True})
    return rango

"""
La funcion creada realiza un widget donde despliega el total de presupuesto , promedio del presupuesto,
"minimo presupuesto", "maximo presupuesto", mostrando como valor pricipal a total de presupuesto 
y para poder identificar el boton se utiliza ddapresupuesto todo esto guardado en la variable 
cambio presupuesto.
"""
def widget_cambios():
    cambio_presupuesto = html.Div([
        dcc.Dropdown(["Total de presupuesto", "Promedio del presupuesto", "Minimo presupuesto", "Maximo presupuesto"],
                     "Total de presupuesto", id="ddapresupuesto")
    ])
    return cambio_presupuesto
"""
Se creo una función dónde el widget  es de opción, este  selecciona uno 
de los botones  que esten en este seria presupuesto total y presupuesto promedio
se pone inline ya que este se cargar de poner los botones de manera horizontal.

"""
def widget_radio():
    comparacion_prs = dcc.RadioItems(["Presupuesto total", "Presupuesto promedio"],
                                     id="radmpresupuesto", value="Presupuesto total", inline=True)
    return comparacion_prs


def widget_rslider(data:pd.DataFrame):                                          #Se realizó una función para la visualizar un botón de rango
    max_val= len(data)                                                          #Sirve para agregar el rango de año que se quiere ver las datos 
    rango = dcc.RangeSlider(1, max_val,10, value=[0, 10], id="ddcalf",
                            tooltip={"placement": "bottom", "always_visible": True})
    return rango


