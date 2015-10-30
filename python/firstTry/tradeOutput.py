#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果

from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture
import time
import json
import sys

#初始化apikey，secretkey,url
apikey = 'db052c78-71e1-4db6-ae7f-f9c659568c30'
secretkey = '93CD90F4E914E8FD08A7DC5423F260C7'
okcoinRESTURL = 'www.okcoin.cn'   #请求注意：国内账号需要 修改为 www.okcoin.cn  
time_sleep = 5

okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)

first_trade_file_log = "/home/ubuntu/firstTrade/firstTradeOutput.log"
first_trade_file_error = "/home/ubuntu/firstTrade/firstTradeOutput.error"
first_trade_file = open(first_trade_file_log, 'a+')
first_trade_error = open(first_trade_file_error, 'a+')

#print (okcoinSpot.trade('btc_cny','buy_market',price=250))
#import pdb; pdb.set_trace()
(symbol, trade_type, price, amount) = sys.argv[1:]


error_count = 0
error_flag = True
while True:
    if error_count >= 10:
        error_log = "%s    %s\n" % (time.strftime("%Y/%m/%d/%H:%M:%S"), "ERROR count exceed!")
        first_trade_error.write(error_log)
        break
    if symbol == 'btc_cny':
        if trade_type == 'buy_market':
            try:
                btc_trade_str = okcoinSpot.trade('btc_cny','buy_market',price)
                btc_trade = json.loads(btc_trade_str)
                if btc_trade['result'] == True:
                    order_id = btc_trade['order_id']
                    while True:
                        try:
                            orderinfo_str = okcoinSpot.orderinfo('btc_cny', str(order_id))
                            orderinfo = json.loads(orderinfo_str)
                            if orderinfo['orders'][0]['status'] == 2:
                                result = {'results': True, 'avg_price': orderinfo['orders'][0]['avg_price'],
                                          'deal_amount': orderinfo['orders'][0]['deal_amount']}
                                print (json.dumps(result))
                                error_flag = False
                                output_log = "%s    BUY_MARKET, price %s, avg_price:%f, deal_amount %f\n" % (time.strftime("%Y/%m/%d/%H:%M:%S"), price, orderinfo['orders'][0]['avg_price'], orderinfo['orders'][0]['deal_amount'])
                                first_trade_file.write(output_log)
                                first_trade_file.flush()
                                break
                        except Exception as e:
                            error_log = "%s    %s\n" % (time.strftime("%Y/%m/%d/%H:%M:%S"), e)
                            first_trade_error.write(error_log)
                            first_trade_error.flush()
                    break
                            
                else:
                    error_log = "%s  BUY_MARKET Failed, price %s,  errorCode %d\n" % (time.strftime("%Y/%m/%d/%H:%M:%S"), price, btc_trade['error_code'])
                    first_trade_file.write(error_log)
                    first_trade_file.flush()
                    break
            except Exception as e:
                error_log = "%s    BUY_MARKET, %s, price:%s, error_count:%d\n" % (time.strftime("%Y/%m/%d/%H:%M:%S"), e, price, error_count)
                first_trade_error.write(error_log)
                first_trade_error.flush()
                error_count += 1

        elif trade_type == 'sell_market':
            try:
                btc_trade_str = okcoinSpot.trade('btc_cny','sell_market',0, amount=str(amount))
                btc_trade = json.loads(btc_trade_str)
                if btc_trade['result'] == True:
                    order_id = btc_trade['order_id']
                    while True:
                        try:
                            orderinfo_str = okcoinSpot.orderinfo('btc_cny', str(order_id))
                            orderinfo = json.loads(orderinfo_str)
                            if orderinfo['orders'][0]['status'] == 2:
                                result = {'results': True, 'avg_price': orderinfo['orders'][0]['avg_price'],
                                          'deal_amount': orderinfo['orders'][0]['deal_amount']}
                                print (json.dumps(result))
                                error_flag = False
                                output_log = "%s    SELL_MARKET, amount %s, avg_price:%f, deal_amount %f\n" % (time.strftime("%Y/%m/%d/%H:%M:%S"), price, orderinfo['orders'][0]['avg_price'], orderinfo['orders'][0]['deal_amount'])
                                first_trade_file.write(output_log)
                                first_trade_file.flush()
                                break
                        except Exception as e:
                            error_log = "%s    %s\n" % (time.strftime("%Y/%m/%d/%H:%M:%S"), e)
                            first_trade_error.write(error_log)
                            first_trade_error.flush()
                    break
                            
                else:
                    error_log = "%s  SELL_MARKET Failed, amount %s, errorCode %d\n" % (time.strftime("%Y/%m/%d/%H:%M:%S"), amount, btc_trade['error_code'])
                    first_trade_file.write(error_log)
                    first_trade_file.flush()
                    break
            except Exception as e:
                error_log = "%s    SELL_MARKET, %s, amount %s, errpr_count: %d\n" % (time.strftime("%Y/%m/%d/%H:%M:%S"), e, amount, error_count)
                first_trade_error.write(error_log)
                first_trade_error.flush()
                error_count += 1


    else:
        error_log = "%s    %s\n" % (time.strftime("%Y/%m/%d/%H:%M:%S"), "No MATCH!!!")
        first_trade_error.write(error_log)
        break

if error_flag:
    error_out = json.dumps({"results": False})
    print (error_out)
#print (okcoinSpot.trade('btc_cny','sell_market',amount=0.1))
#print (okcoinSpot.get_fee('ltc_cny', '185184673'))

first_trade_file.close()
first_trade_error.close()
