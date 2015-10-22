#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果

from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture

#初始化apikey，secretkey,url
apikey = 'db052c78-71e1-4db6-ae7f-f9c659568c30'
secretkey = '93cd90F4E914E8FD08A7DC5423F260C7'
okcoinRESTURL = 'www.okcoin.cn'   #请求注意：国内账号需要 修改为 www.okcoin.cn  

#现货API
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)

#期货API
okcoinFuture = OKCoinFuture(okcoinRESTURL,apikey,secretkey)

print (u' 现货行情 ')
print (okcoinSpot.ticker('btc_usd'))
