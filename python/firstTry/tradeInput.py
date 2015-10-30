#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果

from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture
import time
import json

#初始化apikey，secretkey,url
apikey = 'db052c78-71e1-4db6-ae7f-f9c659568c30'
secretkey = '93CD90F4E914E8FD08A7DC5423F260C7'
okcoinRESTURL = 'www.okcoin.cn'   #请求注意：国内账号需要 修改为 www.okcoin.cn  

#现货API
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)

#期货API
okcoinFuture = OKCoinFuture(okcoinRESTURL,apikey,secretkey)

first_trade_file_log = "/home/ubuntu/firstTrade/firstTradeInput.log"
first_trade_file_error = "/home/ubuntu/firstTrade/firstTradeInput.error"

try:
    first_trade_file = open(first_trade_file_log, 'r')
    first_trade_error = open(first_trade_file_error, 'r')
except Exception:
    first_trade_file = open(first_trade_file_log, 'w')
    first_trade_error = open(first_trade_file_error, 'a+')
else:
    first_trade_file.close()
    first_trade_error.close()
    first_trade_file = open(first_trade_file_log, 'w')
    first_trade_error = open(first_trade_file_error, 'a+')

#print (u' 现货K line ')

while True:
    error_count = 0
    try:
        kline_now = (okcoinSpot.kline(size=4))
        break
    except Exception as e:
        #print (error_count)
        error_count += 1
        pass
since_now=kline_now[2][0]
#print (since_now)
count=0
while count >= 0:
    min1_dist = 60 - int(time.time()) % 60 - 5
    if min1_dist > 0:
        time.sleep(min1_dist)
    error_count = 0
    while True:
        try:
            #print (time.time() % 60)
            kline_now = (okcoinSpot.kline(size=4))
            if kline_now[2][0] <= since_now:
                continue;
            since_now = kline_now[2][0]
            first_trade_file.seek(0)
            first_trade_file.write("date,open,high,low,close,volume\n")
            for i in range(3):
                kline_str = ",".join([str(ele) for ele in kline_now[i]])
                first_trade_file.write("%s\n" % kline_str)
            first_trade_file.flush()
            count = count + 1
            error_count = 0
            break
        except Exception as e:
            first_trade_error.write("%s, %s\n" % (since_now, e))
            if error_count >= 5:
                first_trade_error.write("%s, %s\n" % (since_now, "MAX TRY!!!!!"))
                break
            first_trade_error.flush()

first_trade_file.close()
first_trade_error.close()
