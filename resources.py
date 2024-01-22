from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('Resources', style={'fontSize': 30, 'textAlign': 'left', 'marginBottom': '20px'}), width={"size": 8, "offset": 2})
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(html.P(html.A('Explore the GitHub Repository for more information.', href='https://github.com/MeiMoonHoa/NLP_suicide_ideation_detection', target='_blank'),
                       style={'fontSize': 18, 'textAlign': 'left', 'marginBottom': '20px'}),
                width={"size": 8, "offset": 2})
    ])
], fluid=True)
