from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('Contacts', style={'fontSize':30, 'textAlign':'left', 'marginBottom': '20px'}), width={"size": 8, "offset": 2})
    ]),
    dbc.Row([
        dbc.Col([
            html.H4('Mei Moon Hoa', style={'fontSize':22, 'marginBottom': '10px'}),
            html.P('Postgraduate, Master of Data Science, Faculty of Computer Science and Information Technology, University of Malaya', style={'fontSize':18}),
            html.P(html.A('96meimoon@gmail.com', href='mailto:96meimoon@gmail.com'), style={'fontSize':18}),
            html.P(html.A('GitHub: MeiMoonHoa', href='https://github.com/MeiMoonHoa', target='_blank'), style={'fontSize':18}),
            html.Hr(),
            html.H4('Associate Prof Dr. Kasturi Dewi A/P Varathan', style={'fontSize':22, 'marginBottom': '10px'}),
            html.P('Department of Information System, Faculty of Computer Science and Information Technology, University of Malaya', style={'fontSize':18}),
            html.P(html.A('kasturi@um.edu.my', href='mailto:kasturi@um.edu.my'), style={'fontSize':18}),
        ], width={"size": 8, "offset": 2}),  # Center the column by using offset
    ])
], fluid=True)
