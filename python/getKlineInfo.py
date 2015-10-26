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
secretkey = '93cd90F4E914E8FD08A7DC5423F260C7'
okcoinRESTURL = 'www.okcoin.cn'   #请求注意：国内账号需要 修改为 www.okcoin.cn  

#现货API
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)

#期货API
okcoinFuture = OKCoinFuture(okcoinRESTURL,apikey,secretkey)

try:
    kline_record_file = open("/home/ubuntu/btcKlineRecord.txt", 'r')
    kline_record_error = open("/home/ubuntu/btcKlineRecord.error", 'r')
except Exception:
    kline_record_file = open("/home/ubuntu/btcKlineRecord.txt", 'a+')
    kline_record_file.write("date,open,high,low,close,volume\n")
    kline_record_file.flush()
    kline_record_error = open("/home/ubuntu/btcKlineRecord.error", 'a+')
else:
    kline_record_file.close()
    kline_record_error.close()
    kline_record_file = open("/home/ubuntu/btcKlineRecord.txt", 'a+')
    kline_record_error = open("/home/ubuntu/btcKlineRecord.error", 'a+')

print (u' 现货K line ')

kline_now = (okcoinSpot.kline(size=2))
print (kline_now[0])
since_now=kline_now[0][0]
count=0
while count >= 0:
    time.sleep(20)
    try:
        kline_now = (okcoinSpot.kline(size=2))
        if kline_now[0][0] <= since_now:
            continue;
        print (kline_now[0])
        since_now = kline_now[0][0]
        kline_str = ",".join([str(ele) for ele in kline_now[0]])
        kline_record_file.write("%s\n" % kline_str)
        kline_record_file.flush()
        count = count + 1
    except Exception as e:
        kline_record_error.write("%s, %s\n" % (since_now, e))
        kline_record_error.flush()

kline_record_file.close()
kline_record_error.close()
