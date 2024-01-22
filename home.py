
from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('Welcome to Rebornnn: A New Dawn in Mental Health Support',
        style={'fontSize': 30, 'fontWeight': 'bold', 'textAlign': 'center', 'marginBottom': '20px', 'marginTop': '20px'}))
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(html.P('Rebornnn is at the forefront of harnessing AI to revolutionize how we approach mental health challenges. '
                       'Our application specializes in the early detection of suicide ideation, offering a beacon of hope and support. '
                       'Developed with compassion, respect for privacy, and a commitment to transformative care, '
                       'Rebornnn represents a new beginning for individuals facing mental health struggles, '
                       'providing guidance and light at times when it\'s most needed.',
                       style={'fontSize': 18, 'textAlign': 'justify', 'marginBottom': '20px'}))
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(html.Img(src='/assets/lotus.png', style={'width': '100%', 'height': 'auto', 'maxWidth': '600px', 'marginBottom': '20px'}),
                width={"size": 6, "offset": 3})  # Adjust size and offset as needed
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(html.P('Navigate to the respective page for corresponding functionalities.',
                       style={'fontSize': 20, 'textAlign': 'center','color': '#0a5e11'}))
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(html.Div([
            html.Hr(),
            html.P('Disclaimer:', style={'fontStyle': 'italic'}),
            html.P('The information provided on this application does not and is not intended to constitute legal advice; instead. '
                   'The authors are not liable or responsible for any errors or omissions in the content of this site. '
                   'All information, content, materials, and outcome available on this application are just a prototype provided for '
                   'general informational purposes only. The information contained in this application is provided on an "as is" basis '
                   'with no guarantees of completeness, accuracy, usefulness, or timeliness.',
                   style={'fontSize': 14, 'textAlign': 'justify', 'marginBottom': '20px'}),
            html.P(['Image by ',
                    html.A('OpenClipart-Vectors', href='https://pixabay.com/users/openclipart-vectors-30363/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=150693', target='_blank'),
                    ' from ',
                    html.A('Pixabay', href='https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=150693', target='_blank')],
                   style={'fontSize': 14, 'textAlign': 'center'})
        ]), width=12)
    ]),
    html.Br()
])