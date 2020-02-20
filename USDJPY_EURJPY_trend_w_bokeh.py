# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:10:47 2020

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

url1 = 'https://info.ctfx.jp/service/market/csv/01_USDJPY_D.csv'
url2 = 'https://info.ctfx.jp/service/market/csv/02_EURJPY_D.csv'
res1 = requests.get(url1).content.decode('shift-jis')
res2 = requests.get(url2).content.decode('shift-jis')

df1 = pd.read_csv(io.StringIO(res1))
df2 = pd.read_csv(io.StringIO(res2))
f
df1['date'] = pd.to_datetime(df1['日付'])
df2['date'] = pd.to_datetime(df2['日付'])

df12 = df1.loc[:, ['date','始値','高値','安値','終値']]
df22 = df2.loc[:, ['date','始値','高値','安値','終値']]


p1 = figure(x_axis_type="datetime", title='USDJP & EURJP trend')
p1.grid.grid_line_alpha=0.3
p1.xaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Value'
p1.line(df12['date'], df12['終値'], color='#A6CEE3', legend_label='USDJP')
p1.line(df22['date'], df22['終値'], color='#B2DF8A', legend_label='EURJP')


show(p1)  # open a browser
