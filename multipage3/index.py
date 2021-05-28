
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
from app import app

from layouts import oilLayout
from layouts import oil1Layout
from layouts import oil11Layout
from layouts import oil2Layout
from layouts import oil22Layout
from layouts import oil3Layout
import callbacks


# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "darkslategray",
}
header1={
    "font-family":"courier,arial,helvetica'",
    "background-color":"darkslategray",
    "color":"white"
    }

nav_buttons={
    "border-radius":"16px",
    "font-size":"150%"
    }
# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H1("OIL WELL OPERATION DATA",style=header1),
        html.Hr(style={'color':'red'}),
        html.P(
            "Volume of Oil Produced per Year and Month",
            style=header1
        ),
        dbc.Nav(
            [
                dbc.NavLink("Year Line", href="/apps/Yearline", active="exact",style=nav_buttons),
                dbc.NavLink("Month Line", href="/apps/Monthline", active="exact",style=nav_buttons),
                dbc.NavLink("Year Bar", href="/apps/Yearbar", active="exact",style=nav_buttons),
                dbc.NavLink("Month Bar", href="/apps/Monthbar", active="exact",style=nav_buttons),
                dbc.NavLink("Scatter", href="/apps/scatter", active="exact",style=nav_buttons),
                html.Hr(),
                dbc.NavLink("Oil Prediction", href="/apps/oil", active="exact",
                            style={'border-radius':'16px','background-color':'maroon','color':'white'}),
                
            ],
            vertical=True,
            pills=True,style={'background-color':'darkslategray'},
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/apps/Yearline":
        return oil11Layout 
    elif pathname == "/apps/Monthline":
        return oil1Layout
    elif pathname == "/apps/Yearbar":
        return oil22Layout
    elif pathname == "/apps/Monthbar":
        return oil2Layout
    elif pathname == "/apps/scatter":
        return oil3Layout
    elif pathname == "/apps/oil":
        return oilLayout
    


    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__=='__main__':
    app.run_server(debug=False, port=8060)

