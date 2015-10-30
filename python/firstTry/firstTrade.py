#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果

import pandas as pd
import numpy as np
import dataStruct as data_struct
import os
import json
import time


first_trade_file_log = "/home/ubuntu/firstTrade/firstTradeProcess.log"
first_trade_file_error = "/home/ubuntu/firstTrade/firstTradeProcess.error"
first_trade_file = open(first_trade_file_log, 'a+')
first_trade_error = open(first_trade_file_error, 'a+')

def trade_handler(coin_type, trade_type, price, amount):
    cmd_str = "./tradeOutput.py %s %s %s %s" % (coin_type, str(trade_type), str(price), str(amount))
    trade_output = os.popen(cmd_str)
    trade_result = json.loads(trade_output.readlines()[0])
    return trade_result


def buy_market(coin_type, price, estimated_price=0):
    if  price < 30:
        out_log = "%s    BUY_MARKET Failed, estimated_price %f, price %f less than 30!!\n" % (time.strftime("%Y/%m/%d/%H:%M:%S"), 0, price)
        first_trade_file.write(out_log)
        first_trade_file.flush()
        return False

    result = trade_handler(coin_type, 'buy_market', price, 0)
    if result['results'] == True:
        real_slippage = 0
        return (result['avg_price'], result['deal_amount'])
    else:
        out_log = "%s    BUY_MARKET Failed, estimated_price %f, price %f\n" % (time.strftime("%Y/%m/%d/%H:%M:%S"), 0, price)
        first_trade_file.write(out_log)
        first_trade_file.flush()
        print (out_log)
        return False

def sell_market(coin_type, amount, estimated_price=0):
    if  amount < 0.01:
        out_log = "%s    SELL_MARKET Failed, estimated_price %f, amount %f less than 0.1!!\n" % (time.strftime("%Y/%m/%d/%H:%M:%S"), 0, amount)
        first_trade_file.write(out_log)
        first_trade_file.flush()
        print (out_log)
        return False

    result = trade_handler(coin_type, 'sell_market', 0, amount)
    if result['results'] == True:
        return (result['avg_price'], result['deal_amount'])
    else:
        out_log = "%s    SELL_MARKET Failed, estimated_price %f, amount %f\n" % (time.strftime("%Y/%m/%d/%H:%M:%S"), 0, amount)
        first_trade_file.write(out_log)
        first_trade_file.flush()
        print (out_log)
        return False

data_file = "/home/ubuntu/firstTrade/firstTradeInput.log"
context =data_struct.GlobalData()
#values_list = []
#
def init(cash, coin_type='btc', num=0):
    context.limit_cash = cash
    context.portfolio.positions[coin_type] = num
    context.portfolio.starting_cash = 2000 * num + cash

def loop(k_data, jd_count=3):
    data_lines = len(k_data.index)
    if data_lines < jd_count:
        print ("Wrong k_data")
        return False
    now_item = k_data.loc[jd_count-1]
    done = False
    estimated_price = now_item['close']
    for i in range(jd_count)[::-1]:
        if i == 0:
            price = context.portfolio.cash / 2
            if price > 30:
                result = buy_market('btc_cny', price, now_item['close'])
                if result:
                    avg_price, deal_amount = result
                    real_slippage = (float(avg_price) - float(estimated_price)) / float(estimated_price)
                    out_log = "%s    timestamp %s, BUY_MARKET, estimated_price %f, price %f,  avg_price %f, deal_amount %f, real_slippage %f\n" % (time.strftime("%Y/%m/%d/%H:%M:%S"), time.strftime("%Y/%m/%d/%H:%M:%S", time.localtime(int(now_item['date'])/1000)), estimated_price, price, avg_price, deal_amount, real_slippage)
                    first_trade_file.write(out_log)
                    first_trade_file.flush()
                    print (out_log)
                    context.portfolio.cash -= price
                    context.portfolio.positions['btc'] += deal_amount
                    #context.portfolio.money_order(context.portfolio.cash, now_item['open']*context.slippage)
                    context.order_count += 1
                    context.portfolio.is_buy = 1
            done=True
        elif (k_data.loc[data_lines-i]['close'] <= k_data.loc[data_lines-i-1]['close']):
            break;

    if not done:
        for i in range(jd_count)[::-1]:
            if i == 0:
                amount = context.portfolio.positions['btc'] / 2
                if amount > 0.01:
                    result = sell_market('btc_cny', amount, estimated_price)
                    if result:
                        (avg_price, deal_amount) = result
                        real_slippage = (float(estimated_price) - float(avg_price)) / float(estimated_price)
                        out_log = "%s    timestamp %s,SELL_MARKET, estimated_price %f, amount %f,  avg_price %f, deal_amount %f, real_slippage:%f\n" % (time.strftime("%Y/%m/%d/%H:%M:%S"), time.strftime("%Y/%m/%d/%H:%M:%S", time.localtime(int(now_item['date'])/1000)), estimated_price, amount, avg_price, deal_amount, real_slippage)
                        first_trade_file.write(out_log)
                        first_trade_file.flush()
                        print (out_log)
                        context.offer_count += 1
                        context.portfolio.is_buy = -1
                        context.portfolio.positions['btc'] -= deal_amount
                        context.portfolio.cash += deal_amount * avg_price
            elif (k_data.loc[data_lines-i]['close'] >= k_data.loc[data_lines-i-1]['close']):
                break;
    context.portfolio.update_price(now_item['close'])
    print ("********PRESNET CONDITIONS******************")
    profit_info = "%s    timestamp %s, Profit_info, %s\n" % (time.strftime("%Y/%m/%d/%H:%M:%S"), time.strftime("%Y/%m/%d/%H:%M:%S", time.localtime(int(now_item['date'])/1000)), json.dumps(context.portfolio.get_dict()))
    print (profit_info)
    first_trade_file.write(profit_info)
    first_trade_file.flush()

def is_frame_equal(new_frame, old_frame):
    tmp_frame = pd.merge(new_frame, old_frame)
    if len(tmp_frame.index) < 3:
        return True
    else:
        return False

old_k_data = pd.read_csv(data_file).dropna()
init(100, 'btc', 0)
while True:
    now_item = old_k_data.loc[2]
    print "old_k_data time %s" % (time.strftime("%Y/%m/%d/%H:%M:%S", time.localtime(int(now_item['date'])/1000)))
    min1_dist = 60 - int(time.time()) % 60 - 4
    if min1_dist > 0:
        time.sleep(min1_dist)
    while True:
        k_data = pd.read_csv(data_file).dropna()
        if is_frame_equal(k_data, old_k_data):
            print ("*********NEW DATA*******")
            print (k_data)
            loop(k_data, 3)
            old_k_data = k_data
            break
        else:
            time.sleep(1)

first_trade_file.close()
first_trade_error.close()
