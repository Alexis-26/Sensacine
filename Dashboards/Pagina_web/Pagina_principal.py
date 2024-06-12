import dash                                                #Importamos la librería de Dash
import dash_bootstrap_components as dbc                    #Importamos los componentes de Bootstrap para Dash
from dash import Input, Output, dcc, html                  #Importamos elementos específicos de Dash
from Botones import widgets_dropdown_dir                   #Importamos el primer botón desde Boton_dir_calf
from Botones import widget_rslider                         #Importamos las tarjetas de filtro desde segundo_btn_segundo_dsh
from Botones import widget_cambios                         #Importamos el segundo botón desde x
from Botones import widget_radio                           #Importamos el widget de tiempo desde tercer_btn
from Botones import widget_rslider
from Graficas import graficas_dashboard_1
from Graficas import graficas_dashboard_2
from Graficas import graficas_dashboard_3  

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])     #Declaramos la aplicación Dash con Bootstrap

SIDEBAR_STYLE = {                             #Estilos del menu principal
    "position": "fixed",
    "top": "60px",
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#1b1a1a",
    "z-index": 999,
}

CONTENT_STYLE = {                            #Estilos del contenido
    "margin-left": "18rem",
    "margin-right": "-5rem",
    "padding": "2rem 1rem",
    "margin-top": "60px",  
}

sidebar = html.Div(
    [
        html.P("Menú", className="lead-position"),                                            #Texto de encabezado en el menú
        dbc.Nav(                                                                                   #Navegación en el menú
            [
                dbc.NavLink("Dashboard 1", href="/", active="exact", className="nav-link"),        #Enlace a Dashboard 1
                dbc.NavLink("Dashboard 2", href="/page-1", active="exact", className="nav-link"),  #Enlace a Dashboard 2
                dbc.NavLink("Dashboard 3", href="/page-2", active="exact", className="nav-link"),  #Enlace a Dashboard 3
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
    html.Header(
        [
            html.Img(src="/assets/sensacine1.png", alt="Sensacine", id="logo"),                    #Logo en el encabezado
            html.H1("SENSACINE")                                                                   #Título en el encabezado
        ],
        style={"background": "#faca0a", "padding": "10px 20px", "text-align": "center", "position": "fixed", "top": 0, "left": 0, "width": "100%", "z-index": "1000"}  # Estilos para el encabezado
    ),
    dcc.Location(id="url"),                                                                        #Gestión de la URL
    sidebar,                                                                                       #Barra lateral
    content                                                                                        #Contenido principal
])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")]) #Callback para actualizar el contenido basado en la URL
def render_page_content(pathname, graficas_dashboard_1, graficas_dashboard_2, graficas_dashboard_3):
    if pathname == "/":                                                       #La dirección a la que pertenece esta pagina
        return html.Div(
            [
                html.Main(
                    [
                        html.H2("Directores con mejores calificaciones", style={"font-family": "Lucida Sans, sans-serif", "font-size": "30px", "margin-left": "-50px", "margin-top": "-95px"}, className="lead"),  # Título del Dashboard
                        dbc.Row([
                            dbc.Col(widgets_dropdown_dir(), width=5, className="dropdown-container"),
                            dbc.Col(widget_rslider(), width=7, className="custom-slider"),
                            dbc.Col(graficas_dashboard_1.grafica_barras(), width=12),
                            dbc.Col(graficas_dashboard_1.grafica_caja(), width=12),
                            dbc.Col(graficas_dashboard_1.grafica_scatter(), width=12),
                            dbc.Col(graficas_dashboard_1.grafica_tabla(), width=12)
                        ])                       
                    ],
                    className="container"
                ),
                html.Footer(style={"background": "#333", "padding": "10px 0", "position": "absolute", "bottom": "0", "width": "100%"})  # Pie de página
            ]
        )
    elif pathname == "/page-1":                                       #Contenido para la página 1
        return html.Div(
            [
                html.Main(
                    [
                        html.H2("Distribuidoras con mayor presupuesto", style={"font-family": "Lucida Sans, sans-serif", "font-size": "30px", "margin-left": "-50px", "margin-top": "-95px"}, className="lead"),  # Título del Dashboard
                        dbc.Row([
                            dbc.Col(widget_cambios(), width=12),
                            dbc.Col(graficas_dashboard_2.grafica_barras(), width=12),
                            dbc.Col(graficas_dashboard_2.grafica_pastel(), width=12),
                            dbc.Col(graficas_dashboard_2.grafica_scatter(), width=12),
                            dbc.Col(graficas_dashboard_2.grafica_tabla(), width=12)
                        ])                       
                    ],
                    className="container"
                ),
                html.Footer(style={"background": "#333", "padding": "10px 0", "position": "absolute", "bottom": "0", "width": "100%"})  # Pie de página
            ]
        )
    elif pathname == "/page-2":                                       #Contenido para la página 2
        return html.Div(
            [
                html.Main(
                    [
                        html.H2("Directores con mejores calificaciones", style={"font-family": "Lucida Sans, sans-serif", "font-size": "30px", "margin-left": "-50px", "margin-top": "-95px"}, className="lead"),  # Título del Dashboard
                        dbc.Row([
                            dbc.Col(widget_radio(), width=5, className="dropdown-container"),
                            dbc.Col(widget_rslider(), width=7, className="custom-slider"),
                            dbc.Col(graficas_dashboard_3.grafica_lineas(), width=12),
                            dbc.Col(graficas_dashboard_3.grafica_histograma(), width=12),
                            dbc.Col(graficas_dashboard_3.grafica_barras(), width=12),
                            dbc.Col(graficas_dashboard_3.grafica_tabla(), width=12)
                        ])                       
                    ],
                    className="container"
                ),
                html.Footer(style={"background": "#333", "padding": "10px 0", "position": "absolute", "bottom": "0", "width": "100%"})  # Pie de página
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

if __name__ == "__main__":                                           #Ejecución del servidor en modo debug
    app.run_server(debug=True)
