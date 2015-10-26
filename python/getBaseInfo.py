#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果

from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture
import time

#初始化apikey，secretkey,url
apikey = 'db052c78-71e1-4db6-ae7f-f9c659568c30'
secretkey = '93cd90F4E914E8FD08A7DC5423F260C7'
okcoinRESTURL = 'www.okcoin.cn'   #请求注意：国内账号需要 修改为 www.okcoin.cn  

#现货API
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)

#期货API
okcoinFuture = OKCoinFuture(okcoinRESTURL,apikey,secretkey)

trade_record_file = open("./btcTradeRecord.txt", "a+")
print (u' 现货行情 ')

count = 0
trade_tmp = (okcoinSpot.ticker('btc_usd'))
last_volume = float(trade_tmp['ticker']['vol'])
time.sleep(10)

while count<2:
    trade_now = (okcoinSpot.ticker('btc_usd'))
    print (trade_now)
    date = trade_now['date']
    price = trade_now['ticker']['last']
    sum_volume = float(trade_now['ticker']['vol'])
    volume = sum_volume- last_volume
    record_str = "%s,%s,%d\n" % (date, price, volume)
    trade_record_file.write(record_str)
    last_volume = sum_volume
    count = count + 1
    time.sleep(10)

trade_record_file.close()
