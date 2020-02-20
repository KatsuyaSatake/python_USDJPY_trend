# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:13:36 2020

@author: tfx746
"""
import pandas as pd
import requests
import io
import matplotlib.pyplot as plt
import numpy as np

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
# from bokeh.sampledata.stocks import APPL, GOOG, IBM, MSFT

def datetime(x):
    return np.array(x, dtype=np.datetime64)

url = 'https://info.ctfx.jp/service/market/csv/01_USDJPY_D.csv'
res = requests.get(url).content.decode('shift-jis')

df = pd.read_csv(io.StringIO(res))
df['date'] = pd.to_datetime(df['日付'])

df2 = df.loc[:, ['date','始値','高値','安値','終値']]


p1 = figure(x_axis_type="datetime", title='USDJP trend')
p1.grid.grid_line_alpha=0.3
p1.xaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Value'

p1.line(df2['date'], df2['終値'], color='#A6CEE3', legend_label='USDJP')

show(p1)  # open a browser
