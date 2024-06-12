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

def widget_rslider(data:pd.DataFrame):                                          #Se realizó una función para la visualizar un botón de rango
    max_val= len(data)                                                          #Sirve para agregar el rango de año que se quiere ver las datos 
    rango = dcc.RangeSlider(1, max_val,10, value=[0, 10], id="ddcalf",
                            tooltip={"placement": "bottom", "always_visible": True})
    return rango