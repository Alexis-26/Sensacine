import dash                                                #Importamos la librería de Dash
import dash_bootstrap_components as dbc                    #Importamos los componentes de Bootstrap para Dash
from dash import Input, Output, dcc, html                  #Importamos elementos específicos de Dash
from Dashboards.Widgets.widgets_dash import widgets_dropdown_dir                   #Importamos el primer botón desde Boton_dir_calf
from Dashboards.Widgets.widgets_dash import widget_rslider                         #Importamos las tarjetas de filtro desde segundo_btn_segundo_dsh
from Dashboards.Widgets.widgets_dash import widget_cambios                         #Importamos el segundo botón desde x
from Dashboards.Widgets.widgets_dash import widget_radio                           #Importamos el widget de tiempo desde tercer_btn
from Dashboards.Widgets.widgets_dash import widget_rslider_tiempo
from Dashboards.Graficas import consultas_bd as cbd
from Dashboards.Graficas import graficas_dashboard_1
from Dashboards.Graficas import graficas_dashboard_2
from Dashboards.Graficas import graficas_dashboard_3  

conexionbd = cbd.connect_db()
df1 = cbd.df_director_calificaciones(conexionbd)
df2 = cbd.df_presupuestos_distribuidoras(conexionbd)
df3 = cbd.df_presupuesto_fecha(conexionbd)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])     #Declaramos la aplicación Dash con Bootstrap

SIDEBAR_STYLE = {                             #Estilos del menu principal
    "position": "fixed",
    "top": "100px",
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "padding": "2rem 1rem",
    "background-color": "#1b1a1a",
    "z-index": 999,
    "border": "1px solid #ccc",
    "font-size":"170%",
    "font-family":"Lucida Sans"
}

CONTENT_STYLE = {                            #Estilos del contenido
    "margin-left": "1rem",
    "margin-right": "-1rem",
    "padding": "2rem 1rem",
    "margin-top": "100px",  
}

sidebar = html.Div(
    [
        html.P("Menú", className="lead-position"),                                            #Texto de encabezado en el menú
        html.P("Bienvenido", className="lead-position"),
        dbc.Nav(                                                                                   #Navegación en el menú
            [
                dbc.NavLink("Dashboard 1", href="/", active="exact", className="nav-link", style={"margin-top":"30px"},),        #Enlace a Dashboard 1
                dbc.NavLink("Dashboard 2", href="/page-1", active="exact", className="nav-link", style={"margin-top":"50px"},),  #Enlace a Dashboard 2
                dbc.NavLink("Dashboard 3", href="/page-2", active="exact", className="nav-link", style={"margin-top":"50px"},),  #Enlace a Dashboard 3
            ],
            vertical=True,
            pills=True,
            className="sidebar-nav",
        ),
    ],
    style=SIDEBAR_STYLE,                                                                           #Aplicamos los estilos definidos para el menú
)

content = html.Div(id="page-content", style=CONTENT_STYLE, className="content")

app.layout = html.Div([
    dbc.Navbar(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                [
                                    html.Img(src="/assets/sensacine1.png", alt="Sensacine", id="logo", style={"height": "80px", "max-width": "none"}),
                                    dbc.NavbarBrand("SENSACINE", className="ml-2", style={"color": "#000000", "font-size": "60px", "font-weight":"bold"}),
                                ],
                                style={"display": "flex", "align-items": "center", "justify-content": "center", "height": "100%"}  # Alinea verticalmente el logo y el título
                            ),
                            width={"size": 12, "order": 1}  # La columna ocupa todo el ancho disponible en la fila
                        ),
                    ],
                    align="center",
                    className="flex-nowrap w-100 justify-content-center"
                ),

            ],
            fluid=True
        ),
        color="warning",
        dark=False,
        fixed="top",
        style={"padding": "10px 20px", "text-align": "center"}
    ),
    dcc.Location(id="url"),
    sidebar,
    content
])

@app.callback(Output("page-content", "children"), Input("url", "pathname")) #Callback para actualizar el contenido basado en la URL
def render_page_content(pathname):
    if pathname == "/":
        return html.Div(
            [
                html.Main(
                    [
                        dbc.Row(
                            dbc.Col(
                                html.H2(
                                    "DIRECTORES CON MEJOR CALIFICACIÓN", 
                                    className="lead", 
                                    style={"font-size": "300%","font-family": "Lucida Sans","color": "#ffffff", "text-align": "left", "margin-top": "-95px", "margin-right": "50px", "white-space": "nowrap", "overflow": "hidden", "text-overflow":"ellipsis"}
                                )
                            )
                        ),
                        dbc.Row([
                            dbc.Col(widgets_dropdown_dir(), width=5, className="dropdown-container"),
                            dbc.Col(widget_rslider(df1), width=6, className="custom-slider")]),
                        dbc.Row([
                            dbc.Col(graficas_dashboard_1.grafica_barras(df1), width=5, style={"margin":"20px"}),
                            dbc.Col(graficas_dashboard_1.grafica_caja(df1), width=6, style={"margin":"20px"})]),
                        dbc.Row([
                            dbc.Col(graficas_dashboard_1.grafica_tabla(df1), width=7, style={"margin":"20px"}),
                            dbc.Col(graficas_dashboard_1.grafica_scatter(df1), width=4, style={"margin":"20px"})
                        ]),
                    ],
                    
                ),
            ]
        )
    elif pathname == "/page-1":
        return html.Div(
            [
                html.Main(
                    [
                        dbc.Row(
                            dbc.Col(
                                html.H2(
                                    "DISTRIBUIDORAS CON MAYOR PRESUPUESTO", 
                                    className="lead", 
                                    style={"font-size": "300%","font-family": "Lucida Sans","color": "#ffffff", "text-align": "left", "margin-top": "-95px", "margin-right": "50px", "white-space": "nowrap", "overflow": "hidden", "text-overflow":"ellipsis"}
                                )
                            )
                        ),
                        dbc.Row(dbc.Col(widget_radio(), width=3)),
                        dbc.Row([
                            dbc.Col(graficas_dashboard_2.grafica_barras(df2), width=5, style={"margin":"20px"}),
                            dbc.Col(graficas_dashboard_2.grafica_scatter(df2), width=6, style={"margin":"20px"} )]),
                        dbc.Row([
                            dbc.Col(graficas_dashboard_2.grafica_tabla(df2), width=6, style={"margin":"20px"}),
                            dbc.Col(graficas_dashboard_2.grafica_pastel(df2), width=5, style={"margin":"20px"})
                        ]),
                    ],
                ),
            ]
        )
    elif pathname == "/page-2":
        return html.Div(
            [
                html.Main(
                    [
                        dbc.Row(
                            dbc.Col(
                                html.H2(
                                    "PRESUPUESTO DE LAS PELÍCULAS A LO LARGO DEL TIEMPO", 
                                    className="lead", 
                                    style={"font-size": "300%","font-family": "Lucida Sans","color": "#ffffff", "text-align": "left", "margin-top": "-95px", "margin-right": "50px", "white-space": "nowrap", "overflow": "hidden", "text-overflow":"ellipsis"}
                                )
                            )
                        ),
                        dbc.Row([
                            dbc.Col(widget_cambios(), width=12, className="dropdown-container"),
                            dbc.Col(widget_rslider_tiempo(df3), width=7, className="custom-slider")]),
                        dbc.Row([
                            dbc.Col(graficas_dashboard_3.grafica_tabla(df3), width=11, style={"margin":"20px"})
                        ]),
                        dbc.Row([
                            dbc.Col(graficas_dashboard_3.grafica_lineas(df3), width=11, style={"margin":"20px"}),
                        ]),
                        dbc.Row([
                            dbc.Col(graficas_dashboard_3.grafica_barras(df3), width=5, style={"margin":"20px"}),
                            dbc.Col(graficas_dashboard_3.grafica_histograma(df3), width=5, style={"margin":"20px"})
                        ]),
                    ],
                ),
            ]
        )
    return html.Div(                                                  #Contenido para página no encontrada (404)
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )