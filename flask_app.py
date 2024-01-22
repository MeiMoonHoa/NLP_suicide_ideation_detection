from flask import Flask
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Initialize the Flask server
server = Flask(__name__)

# Initialize the Dash app with Flask as the server backend
app = dash.Dash(
    server=server,
    external_stylesheets=[dbc.themes.COSMO],
    suppress_callback_exceptions=True
)

# Dynamically import page layouts to avoid circular imports
# This allows for modular design and better separation of concerns
from home import layout as home_layout
from resources import layout as resources_layout
from contacts import layout as contacts_layout
from applications import layout as applications_layout

# Define the global layout of the Dash app
# Includes a navigation bar and a content container that will hold the page content

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(
        "Suicide Ideation Prediction System",
        style={'fontSize': 50, 'textAlign': 'center', 'color': '#023328'}  # Change title color to match the nav
    ),
    html.Hr(),
    dbc.Nav(
        [
            dbc.NavItem(dbc.NavLink("<< Home >>", href="/", style={
                'color': 'white', 'fontSize': 20, 'fontWeight': 'bold', 'padding': '10px'})),
            dbc.NavItem(dbc.NavLink("<< Resources >>", href="/resources", style={
                'color': 'white', 'fontSize': 20, 'fontWeight': 'bold', 'padding': '10px'})),
            dbc.NavItem(dbc.NavLink("<< Contacts >>", href="/contacts", style={
                'color': 'white', 'fontSize': 20, 'fontWeight': 'bold', 'padding': '10px'})),
            dbc.NavItem(dbc.NavLink("<< Application >>", href="/applications", style={
                'color': 'white', 'fontSize': 20, 'fontWeight': 'bold', 'padding': '10px'})),
        ],
        className='nav nav-pills justify-content-center',
        style={
            'backgroundColor': '#023328',
            'padding': '12px',
            'border': '2px solid white',  # Adding a white border
            'borderRadius': '8px',  # Optional: rounded corners for the nav bar
        },
    ),
    html.Hr(),
    html.Div(id='page-content'),
]
)


# Callback to dynamically change the page content based on the URL path
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    # Depending on the URL path, return the corresponding page layout
    if pathname == '/':
        return home_layout
    elif pathname == '/resources':
        return resources_layout
    elif pathname == '/contacts':
        return contacts_layout
    elif pathname == '/applications':
        return applications_layout
    else:
        # As a fallback for unknown paths, return the home layout
        return home_layout

# Conditional to ensure the server only runs in development/local mode
# In production, especially when deployed on PythonAnywhere, this should be commented out
if __name__ == '__main__':
    # The host='0.0.0.0' makes the app accessible on your local network.
    # Remove it if you only want to access the app on your local machine
    app.run_server(debug=True)
