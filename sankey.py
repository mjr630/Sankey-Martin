# -*- coding: utf-8 -*-
"""
18/10/2021
Isabella Merriman and Martin Roberti
ENCN493-RPE04
Embodied carbon in New Zealand's Energy System
Sankey
"""
# format retrieved from https://plotly.com/python/sankey-diagram/

import plotly.graph_objects as go

def call_data(): 
    """retrieve data from csv"""

def sankey_plot():
    """sankey funtion for making the sanky diagram"""
    fig = go.Figure(data=[go.Sankey(
        node = dict(
            pad = 15,
            thickness = 20,
            line = dict(color = "black", width = 0.5),
            label = [" ", " ", " ",],
            color = "blue"
            ),
        link = dict(
            source = [0, 1, 0, 2], # indices correspond to labels, eg A1, A2, etc
            target = [2, 3, 3, 4],
            value = [8, 4, 2, 8]
            ))])

    fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
    fig.show()
    

def main():
    """main function that opens specific funtions"""
    () = call_data()
    () = sankey_plot()
