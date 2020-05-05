# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from utils import read_data
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

river_height_data = read_data("braided-river")
sh_0, sh_1 = river_height_data.shape[1:]

fig = go.Figure(data=[go.Surface(z=river_height_data[500],
                                 contours={
                                     "x": {"show": False},
                                     "y": {"show": False},
                                     "z": {"show": True, "start": 5000000, "end": 14000000,
                                           "size": 1500000, "color": 'white'}
                                 }
                                 )],

                )
fig.update_layout(title='River', autosize=False,
                  scene=dict(aspectmode='manual',
                             aspectratio = dict(x=10, y=1, z=0.5)),
                  width=1500,
                  height=750,
                  margin=dict(r=20, l=10, b=10, t=10))


app.layout = html.Div(children=[
    html.H1(children='Braided River'),

    html.Div(children='''
        A visualisation of the progression of a braided river
    '''),

    dcc.Graph(
        id='river_graph',
        figure=fig
    ),

    dcc.Slider(
        id='frame_selector',
        min=0,
        max=len(river_height_data) - 1,
        step=1,
        value=250,
    ),

])

camera = dict(
    eye=dict(x=0., y=5., z=4.)
)

@app.callback(
    dash.dependencies.Output('river_graph', 'figure'),
    [dash.dependencies.Input('frame_selector', 'value')])
def update_output(value):
    fig = go.Figure(data=[go.Surface(z=river_height_data[value],
                                     contours={
                                         "x": {"show": False},
                                         "y": {"show": False},
                                         "z": {"show": True, "start": 5000000, "end": 14000000, "size": 1500000,
                                               "color": 'white'}
                                     }
                                     )])
    fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                      highlightcolor="limegreen", project_z=True))
    fig.update_layout(title='River', autosize=False,
                      scene_camera = camera,
                      scene=dict(aspectmode='manual',
                                 aspectratio=dict(x=10, y=1, z=0.5)),
                      width=1500,
                      height=750,
                      margin=dict(r=20, l=10, b=10, t=10))
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)