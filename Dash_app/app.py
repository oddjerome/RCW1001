
import Dash_app
from dash import html, dash, dcc

# initialiser " application dash
app = dash.Dash(__name__, requests_pathname)


# definir Dash
app.layout = html.Div(children=[
    html.Div([
        html.A('Accueil', href="/"),
        "|",
        html.A("Logout", href="/logout")
    ])
])