#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 23:14:13 2019

@author: Shark
"""

import tushare as ts
from pyecharts.charts import Line,Kline
from pyecharts import options as opts

hist_data = ts.get_hist_data('000333')
hist_data.round(2)
hist_data.to_csv('/Users/mac/Desktop/data.csv')

x = hist_data.index.tolist()
y_data = hist_data[['open','close','low','high']].values.tolist()
ma5 = hist_data['ma5']
ma10 = hist_data['ma10']

x.reverse()
y_data.reverse()
print(x)



x1 = hist_data.index.tolist()[:20]
y1 = hist_data['open'].iloc[:20]
y2 = hist_data['close'].iloc[:20]

#Line-折线图
line = Line().add_xaxis(x1).add_yaxis('开盘价',y1,is_smooth=True).add_yaxis('收盘价',range(20),is_smooth=True)   
line.render('/Users/mac/Desktop/fig.html') 

#K-line图   

#K_line = Kline().add_xaxis(x).add_yaxis('美的集团-000333',y_data).set_global_opts(datazoom_opts=[opts.DataZoomOpts(type_="inside")])
#K_line.render('/Users/mac/Desktop/fig1.html') 
K_line = Kline().add_xaxis(x).add_yaxis('美的集团-000333',							y_data,markline_opts=opts.MarkLineOpts([opts.MarkLineItem(type_='max',value_dim='close')]),).set_global_opts(datazoom_opts=[opts.DataZoomOpts(type_="inside")])
K_line.render('/Users/mac/Desktop/fig1.html') 
