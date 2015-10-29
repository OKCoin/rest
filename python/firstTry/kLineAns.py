#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果

import pandas as pd
import numpy as np
import dataStruct as data_struct


std1 = 0.68
std2 = 0.95

k_data = pd.read_csv("./t_all.csv")
#k_data = pd.read_csv("./t.csv")
log_file = open("./kLine1.log", "w+")

vol_data = k_data['volume']
price_data = k_data['close']

vol_desc = vol_data.describe()
price_desc = price_data.describe()
print ("Volume---> min: %f, max:%f, mean:%f, std:%f") % (vol_data.min(), vol_data.max(), vol_desc['mean'], vol_desc['std'])
print ("Price--->  min: %f, max:%f, mean:%f, std:%f") % (price_data.min(), price_data.max(), price_desc['mean'], price_desc['std'])
#print (k_data)
import pdb;pdb.set_trace()

context =data_struct.GlobalData()
values_list = []

def init(cash):
    context.limit_cash = 5000
    #context.slippage = 1 - 0.000246
    context.slippage = 1

def loop(jd_count=2):
    data_lines = len(k_data.index)
    for time_slice in xrange(data_lines):
        context.portfolio.is_buy = 0
        if time_slice < jd_count:
                   values_list.append(context.portfolio.get_dict())
                   continue
        now_item = k_data.loc[time_slice]
        done = False
        for i in range(jd_count)[::-1]:
            if i == 0:
                context.portfolio.money_order(context.portfolio.cash, now_item['open']*context.slippage)
                context.order_count += 1
                done=True
            elif (k_data.loc[time_slice-i+1]['close'] <= k_data.loc[time_slice-i]['close']):
                break;

        if not done:
            for i in range(jd_count)[::-1]:
                if i == 0:
                    context.portfolio.count_order(-context.portfolio.positions['btc'], now_item['open']*context.slippage)
                    context.offer_count += 1
                elif (k_data.loc[time_slice-i+1]['close'] >= k_data.loc[time_slice-i]['close']):
                    break;
        context.portfolio.update_price(now_item['close'])
        values_list.append(context.portfolio.get_dict())

init(5000)
loop(3)
print ("************************FINAL RESULT*****************************")
final_value = context.portfolio.get_dict()
print (final_value)
print ("order count:%d and offer count:%d") % (context.order_count, context.offer_count)
values_data = pd.DataFrame(values_list)
print ("**********************DETAILS MAX****************************")
print (values_data[['market_value','total_returns','daily_returns']].max())
print ("**********************DETAILS MIN****************************")
print (values_data[['market_value','total_returns','daily_returns']].min())
#print ("**********************DETAILS****************************")
values_data.to_csv(log_file)
#print (values_data)
log_file.close()
