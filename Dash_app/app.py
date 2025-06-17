import dash
from dash import html, dcc, Output, Input
import requests

app = dash.Dash(
    __name__,
    requests_pathname_prefix="/dashboard/"
)

app.layout = html.Div([
    html.Div([
        html.A('Accueil', href='/')
    ], style={'marginTop': 25}),

    html.Div(id="info-div"),
    dcc.Interval(id="refresh", interval=10*1000, n_intervals=0),  # actualisation toutes les 10s

    dcc.Graph(
        id="exmpl-1",
        figure={
            "data": [
                {"x": [2, 5, 7], "y": [8, 3, 9], "type": "bar", "name": "exmp1"},
                {"x": [5, 3, 8], "y": [6, 2, 5], "type": "bar", "name": "exmp2"}
            ]
        }
    ),
    html.H2("*** scatter Plot Graph *** "),
    dcc.Graph(
        id="exm3",
        figure={
            "data":[
                {"x":[1,3,5,7], "y":[10,12,14,16], "type":"scatter", "mode":"markers", "name":"scatter exmpl1"},
                {"x":[2,4,6,8], "y":[13,15,17,19], "type":"scatter", "mode":"markers", "name":"scatter exmpl2"}
            ]
        }
    ),
    
    html.H2("*** Pie Chart Graph *** "),
    dcc.Graph(
        id="exm4",
        figure={
            "data":[
                {"labels":["A","B","C"], "values":[10,12,14], "type":"pie", "name":"pie chart expl1"},
            ],
            "layout":{"title":"pie chart example"}
        }
    ),
])

@app.callback(
    Output("info-div", "children"),
    Input("refresh", "n_intervals")
)
def load_info(n):
    try:
        response = requests.get("http://localhost:8001/api/info")
        if response.status_code == 200:
            info = response.json()
            return html.Div([
                html.H3(f"Aujourd'hui est {info['date']} et il est {info['time']}"),
                html.P(f"City : {info['weather']['city']}"),
                html.P(f"Temperature : {info['weather']['temperature']}"),
                html.P(f"Description : {info['weather']['description']}")
            ])
        else:
            return html.P("Erreur de chargement des données")
    except Exception as e:
        return html.P(f"Erreur : {str(e)}")

server = app.server
