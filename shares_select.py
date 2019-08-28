'''
@Descripttion: 
    筛选目标：
    1、选取天>7%或者月涨幅>10%
    2、净利润>2000w，且增速>20%
    3、5均线>10均线
    4、近2月跌幅>30%
    5、医药或者科技板块
    6、在此基础上筛选增速>100%
@version: 1.0
@Author: Crazy_G
@Date: 2019-08-27 23:14:27
@LastEditors: Crazy_G
@LastEditTime: 2019-08-28 23:46:09
'''
import re
import sqlite3

import pandas as pd
import tushare as ts
from sqlalchemy import create_engine


#获取当天全部股票数据并存入sqlite数据库
def get_t_data():
    engine = create_engine('sqlite:///all_data.db?check_same_thread=False', echo=True)
    #获取当天股票数据，并存入数据库
    t_data = ts.get_today_all()
    t_data.to_sql('t_data',engine)

    #获取非ST股票数据
    norm_data = t_data[~t_data['name'].str.contains('ST')]
    norm_data.to_sql('norm_data',engine)
    #获取非ST股票code,name
    norm_data = norm_data[['code','name']]
    norm_data.to_sql('cn_data',engine)
    
    #获取ST股票数据
    st_data = t_data[t_data['name'].str.contains('ST')]
    st_data.to_sql('st_data',engine)



