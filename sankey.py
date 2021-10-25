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
    print(rdf)
    return rdf, ndf

    
        

    
    
def sankey_plot(rdf, ndf):
    """sankey funtion for making the sanky diagram"""
    """supply"""
    fig = go.Figure(data=[go.Sankey(
        node = dict(
            pad = 15,
            thickness = 20,
            line = dict(color = "black", width = 0.5),
            label = ["Hydropwer 0", "Geothermal 1", "Solar 2","wind 3", "Biogas 4", "Solid Biofuels 5", "Liquid Biofuels 6",
                     "electricity 7", "Cogeneration 8","Oil Products production 9", "direct use 10", "Agriculture 11",
                     "Industrial 12", "Comercial 13", "Residential 14", "Direct Energy Consumption 15", 
                     "natural gas 16", "distribution losses 17", "gas flared 18", "production losses and own use 19", "Transport 20"],
            color = "blue"
            ),
        link = dict(
            source = [0, 1, 2, 3, 4, 5, 6, 7, 1, 4, # Renewables
                      5, 6, 1, 2, 5, 10, 10, 10, 10, 7,
                      8, 9,
                      16, 16, 16, 16, 16, 16, 10, 10, 10, 10, 10, 7, 8], 
            target = [7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 
                      8, 9, 10, 10, 10, 11, 12, 13, 14, 15,
                      15, 15,
                      7, 8, 17, 18, 19, 10, 11, 12, 13, 14, 20, 15, 15], 
            value = [rdf.at[11,'E'],rdf.at[12,'E'],rdf.at[13,'E'],rdf.at[14,'E'],rdf.at[15,'E'],0,0, 0, rdf.at[17,'E'],rdf.at[18,'E'],
                     rdf.at[19,'E'], rdf.at[20,'E'], rdf.at[35,'E'], rdf.at[36,'E'],rdf.at[37,'E'], rdf.at[22,'E'], rdf.at[24,'E'], rdf.at[28,'E'], rdf.at[30,'E'], rdf.at[10,'E'],
                     rdf.at[16,'E'], rdf.at[20,'E'],
                     ndf.at[7,'E'], ndf.at[8,'E'], ndf.at[11,'E'], ndf.at[4,'E'], ndf.at[10,'E'], ndf.at[12,'E'],ndf.at[13,'E'],ndf.at[14,'E'], ndf.at[15,'E'], ndf.at[16,'E'], ndf.at[17,'E'], ndf.at[7,'E'], ndf.at[8,'E'] ]
            ))])


    fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
    plot(fig)
    

def main():
    """main function that opens specific funtions"""
    rdf, ndf = call_data()
    sankey_plot(rdf, ndf)
    
main()
