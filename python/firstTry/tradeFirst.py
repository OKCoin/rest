#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果

from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture
import time

#初始化apikey，secretkey,url
apikey = 'db052c78-71e1-4db6-ae7f-f9c659568c30'
secretkey = '93CD90F4E914E8FD08A7DC5423F260C7'
okcoinRESTURL = 'www.okcoin.cn'   #请求注意：国内账号需要 修改为 www.okcoin.cn  
time_sleep = 5

#现货API
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)

trade_record_file = open("./btcTradeRecord.txt", "a+")
print (u'Trade Info ')

#print (okcoinSpot.trade('btc_cny','buy_market',price=250))
#print (okcoinSpot.trade('btc_cny','sell_market',amount=0.1))

print (u' 现货订单信息查询 ')
print (okcoinSpot.orderinfo('btc_cny', '185184673'))
print (okcoinSpot.get_fee('btc_cny', '185184673'))

trade_record_file.close()
