from dash import html, dcc, Dash, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np
import re
import emoji
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer


from concurrent.futures import ThreadPoolExecutor
from dash.exceptions import PreventUpdate

# Create a Dash instance
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Expose the Flask server for WSGI to use
server = app.server

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("/home/meimoonhoa/mysite")
model = AutoModelForSequenceClassification.from_pretrained('/home/meimoonhoa/mysite')
model.eval()  # Set model to evaluation mode

# Function to clean and preprocess text
def preprocess_text(text):
    # Convert emojis to text
    text = emoji.demojize(text)

    # Simplify punctuation
    text = re.sub(r'(\!)\1{2,}', r'\1', text)  # Simplify exclamation marks
    text = re.sub(r'(\?)\1{2,}', r'\1', text)  # Simplify question marks
    text = re.sub(r'(\.)\1{2,}', r'\1', text)  # Simplify periods

    # Remove URLs, user mentions, and special characters
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'u/\w+|r/\w+|@\w+', '', text)
    text = re.sub(r"[^a-zA-Z0-9.,'\u2019]+", ' ', text)

    # Remove extra whitespaces
    text = re.sub(r'\s\s+', ' ', text).strip()

    # Tokenize and remove stop words
    tokenizer = RegexpTokenizer(r'\w+')
    stop_words_set = set(stopwords.words("english"))
    words = tokenizer.tokenize(text.lower())
    clean_words = [word for word in words if word not in stop_words_set]

    # Rejoin words
    return ' '.join(clean_words)

# Define the layout of the application page
layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('Try out the application!!!',
        style={'fontSize': 30, 'fontWeight': 'bold', 'textAlign': 'center', 'marginBottom': '20px', 'marginTop': '20px'}))
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(html.P("To start, simply input or paste text into the field below. Our tool will analyze the text for potential signs of suicide ideation.",
                       style={'fontSize': 18, 'textAlign': 'center', 'marginBottom': '20px'}), width=12)
    ]),
    dbc.Row([
        dbc.Col(dcc.Textarea(id='text_input', placeholder='Enter text here...',
                             style={'width': '80%', 'height': 200, 'padding': '10px', 'marginLeft': '10%'}), width=12)
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(html.Button('Analyze', id='analyze_button', n_clicks=0,
                            className='btn btn-lg', style={'fontSize': '20px', 'fontWeight': 'bold','width': '50%', 'padding': '10px', 'marginLeft': '25%','backgroundColor': '#18b892', 'color': 'white', 'border': 'none'}),
                width=12)
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(dcc.Loading(html.Div(id='result_container'), style={'textAlign': 'center'}), width=12)
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
        ]), width={"size": 10, "offset": 1})
    ]),
], fluid=True)

app.layout = layout



# Create a thread pool executor for running inference in a background thread
executor = ThreadPoolExecutor(max_workers=1)

# Define the function that will run model inference
def run_inference(inputs):
    with torch.no_grad():
        outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits, axis=1).item()
    return prediction

# Define the callback for the Analyze button
@callback(
    Output('result_container', 'children'),
    [Input('analyze_button', 'n_clicks')],
    [State('text_input', 'value')]
)
def update_output(n_clicks, text_input):
    if text_input is None or n_clicks is None:
        raise PreventUpdate  # Prevents callback re-execution if conditions aren't met

    # Preprocess the input text
    cleaned_input_text = preprocess_text(text_input)

    # Tokenize the preprocessed text for the model
    inputs = tokenizer(cleaned_input_text, return_tensors="pt", padding=True, truncation=True, max_length=512)

    # Start the model prediction in a separate thread
    future = executor.submit(run_inference, inputs)

    # Wait for the inference to complete (with a timeout, if desired)
    try:
        prediction = future.result(timeout=10)  # Waits for at most 10 seconds
    except concurrent.futures.TimeoutError:
        return html.Div("Model inference timed out. Please try again.", style={'color': 'red'})

    # Style the result display
    result_style = {
        'color': 'white',  # Text color set to white for contrast
        'fontWeight': 'bold',
        'fontSize': 20,
        'border': '2px solid',
        'borderColor': 'red' if prediction == 1 else 'green',
        'padding': '10px',
        'borderRadius': '5px',
        'margin': '20px',
        'textAlign': 'center',
        'backgroundColor': '#D32F2F' if prediction == 1 else '#4CAF50'  # Red for related, green for not related
    }

    # Display the result based on the prediction
    if prediction == 1:
        return html.Div("The analysis indicates this text is RELATED to suicide ideation.", style=result_style)
    else:
        return html.Div("The analysis indicates this text is NOT RELATED to suicide ideation.", style=result_style)


# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)
