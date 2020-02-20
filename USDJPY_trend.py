# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 12:02:59 2020
"""

import pandas as pd
import requests
import io
import matplotlib.pyplot as plt

url = 'https://info.ctfx.jp/service/market/csv/01_USDJPY_D.csv'
res = requests.get(url).content.decode('shift-jis')

df = pd.read_csv(io.StringIO(res))
df['date'] = pd.to_datetime(df['日付'])

df2 = df.loc[:, ['date','始値','高値','安値','終値']]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(df2['date'], df2['終値'])
ax.grid(True)