# -*- coding: utf-8 -*-
import httplib
import urllib
import json
import md5
import time

class OKCoin():
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def __signature(self, params):
        s = ''
        for k in sorted(params.keys()):
            if len(s) > 0:
                s += '&'
            s += k + '=' + str(params[k])
        return md5.new(s + '&secret_key='+self.api_secret).hexdigest().upper()

    def __tapi_call(self, method, params={}):
        params["partner"] = self.api_key
        params["sign"] = self.__signature(params)
        headers = {
            "Content-type" : "application/x-www-form-urlencoded",
        }
        conn = httplib.HTTPSConnection("www.okcoin.cn", timeout=10) # 注意国际站 需要将 www.okcoin.cn 换成www.okcoin.com
        temp_params = urllib.urlencode(params)
        conn.request("POST", "/api/v1/%s.do" % method, temp_params, headers)
        response = conn.getresponse()
        data = json.load(response)
        params.clear()
        conn.close()
        #print data
        res = data.get("result")
        if res == "true" or res == True:
            return data
        else:
            raise Exception("error code %s" % data["error_code"])

    def __api_call(self, method, pair):
        conn = httplib.HTTPSConnection("www.okcoin.cn", timeout=10) # 注意国际站 需要将 www.okcoin.cn 换成www.okcoin.com
        conn.request("GET", "/api/v1/%s.do?symbol=%s" % (method, pair))
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data

    def get_ticker(self, pair):
        data = self.__api_call("ticker", pair)
        if "ticker" in data:
            return {
                "last": data["ticker"]["last"],
                "buy": data["ticker"]["buy"],
                "sell": data["ticker"]["sell"],
                "vol": data["ticker"]["vol"]
            }
        else:
            raise Exception("Error when get ticker")

    def get_depth(self, pair):
        return self.__api_call("depth", pair)

    def get_funds(self):
        return self.__tapi_call('userinfo')

    def get_orders(self, pair, order_id=-1):
        params = { "symbol"   : pair, "order_id" : order_id }
        result = self.__tapi_call('order_info', params)
        return result["orders"]

    def trade(self, tpair, ttype, price, amount):
        params = {
            "symbol" : tpair, # 国际站：btc_usd/ltc_usd  国内站  btc_cny/ltc_cny
            "type"   : ttype,
            "price"   : price,
            "amount" : amount
        }
        result = self.__tapi_call('trade', params)
        return result["order_id"]

    def buy(self, pair, price, amount):
        result = self.trade(pair, "buy", price, amount)
        return result

    def sell(self, pair, price, amount):
        result = self.trade(pair, "sell", price, amount)
        return result

    def cancel(self, pair, order_id):
        params = { "symbol": pair, "order_id" : order_id }
        return type(self.__tapi_call('cancel_order', params)) == dict

