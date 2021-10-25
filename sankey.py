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
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import interpolate
import statistics
from scipy.optimize import fsolve
import math
from plotly.offline import download_plotlyjs, init_notebook_mode,  plot
from plotly.graph_objs import *
init_notebook_mode()



def call_data(): 
    """retrieve data from csv"""
    cdf = pd.DataFrame(pd.read_csv('Coal_data.csv'))
    odf = pd.DataFrame(pd.read_csv('Oil_data.csv'))
    ndf = pd.DataFrame(pd.read_csv('Naturalgas_data.csv'))
    rdf = pd.DataFrame(pd.read_csv('Renewables_data.csv'))
    #print(coal_dataframe)
    #print(oil_dataframe)
    #print(naturalgas_dataframe)
    print(rdf.at[0,'E'])
    return rdf

    
        

    
    
def sankey_plot(rdf):
    """sankey funtion for making the sanky diagram"""
    """supply"""
    fig = go.Figure(data=[go.Sankey(
        node = dict(
            pad = 15,
            thickness = 20,
            line = dict(color = "black", width = 0.5),
            label = ["Hydropwer", "Geothermal", "Solar","wind", "Biogas", "Solid Biofuels", "Liquid Biofuels"
                     "Hydropwer", "Geothermal", "Solar","wind", "Biogas", "Solid Biofuels", "Liquid Biofuels"],
            color = "blue"
            ),
        link = dict(
            source = [0, 0, 0, 0, 0, 0, 0, 
                      1, 1, 1, 1, 1, 1, 1], # indices correspond to labels, eg A1, A2, etc
            target = [1, 1, 1, 1, 1, 1, 1, 
                      2, 2, 2, 2, 2, 2, 2],
            value = [2,3,7,8,5,4,3,
                     2,3,8,5,7,6,5]
            ))])


    fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
    plot(fig)
    

def main():
    """main function that opens specific funtions"""
    rdf = call_data()
    sankey_plot(rdf)
    
main()
