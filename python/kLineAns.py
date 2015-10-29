#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果

import pandas as pd
import numpy as np
import dataStruct as data_struct

std1 = 0.68
std2 = 0.95

k_data = pd.read_csv("./t.csv")

vol_data = k_data['volume']
price_data = k_data['close']

vol_desc = vol_data.describe()
price_desc = price_data.describe()
print ("Volume---> min: %f, max:%f, mean:%f, std:%f") % (vol_data.min(), vol_data.max(), vol_desc['mean'], vol_desc['std'])
print ("Price--->  min: %f, max:%f, mean:%f, std:%f") % (price_data.min(), price_data.max(), price_desc['mean'], price_desc['std'])
import pdb;pdb.set_trace()

context =data_struct.GlobalData

def init():
    context.limit_cash = 5000

def loop():
    data_lines = len(k_data.index)
    for time_slice in xrange(data_linesi+1):
        if time_slice < 2:
            continue
        
    

def handle_bar(k_data):
    pass
