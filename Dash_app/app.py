import dash
from dash import html, dcc

app = dash.Dash(
    __name__,
    requests_pathname_prefix="/dashboard/"
)

app.layout = html.Div([
    html.Div([
        html.A('Accueil', href='/')
    ], style={'marginTop': 25}),
    
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
                {"x":[1,3,5,7], "y":[10,12,14,16] , "type":"scatter" , "mode":"markers","name":"scatter exmpl1"},
                {"x":[2,4,6,8], "y":[13,15,17,19] , "type":"scatter" , "mode":"markers","name":"scatter exmpl2"}
            ]
        }
    ),
    
    html.H2("*** Pie Chart Graph *** "),
    dcc.Graph(
        id="exm4",
        figure={
            "data":[
                {"labels":["A","B","C"], "y":[10,12,14] , "type":"pie" , "name":"pie chart expl1"},
            ],
            "layout":{"title":"pie chart example"}
        }
    )
])

server = app.server
