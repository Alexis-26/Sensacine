def widgets_dropdown_dir():                                                     #Se realizó una función para la visualización de un botón desplegable
    califdir = html.Div([                   
    dcc.Dropdown(["Usuarios", "Medios", "Sensacine"], "Usuarios", id="tcalf",) #Se despliega usuarios, medios y sensacine, predeterminando viaualizualmente Usuarios
    ])                                                                         #Se le agrega un id para llamarlo en el callback
    return califdir
