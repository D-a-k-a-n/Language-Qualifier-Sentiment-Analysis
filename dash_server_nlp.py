# import dash
from dash import Dash, dcc, html, Input, Output, State
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    children = [
        html.H1(id='heading1', children='Hello Dash'),
        html.Hr(),

        html.P(id='heading2', children='Type your text!',
                           className='display-3 mb-4', style={'width':'4000px', 'font': 'sans-seriff', 'font-weight': 'bold', 'font-size': '30px', 'color': 'black'}),
        dcc.Textarea(id='input_text', className="mb-3", placeholder="Enter a review",
                                 value='', style={'resize': 'none'}),

        html.Div(id='output_language', style={'whiteSpace': 'pre-line'}),
        html.Div(id='output_result', style={'whiteSpace': 'pre-line'})
    ]
)

@app.callback(Output('output_language', 'children'),
              [Input('input_text', 'value')]
)
def update_output(value):
  return 'You Language is: None'

@app.callback(Output('output_result', 'children'),
              [Input('input_text', 'value')]
)
def update_output(value):
  return 'Text is Positive?: Yes!'


app.run_server(debug=True)