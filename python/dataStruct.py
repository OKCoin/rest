#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8


class Portfolio(object):
    def __init__(self, cash=0.0):
        self.starting_cash = cash
        self.cash = cash
        self.total_returns = 0.0
        self.daily_returns = 0.0
        self.prev_value = cash
        self.market_value = cash
        self.positions = {'btc': 0.0, 'ltc': 0.0}
        self.prices = {'btc': 0.0, 'ltc': 0.0}
        self.is_buy = 0

    def get_dict(self, pos_key='btc'):
        return {'cash': self.cash,
                'total_returns': self.total_returns,
                'daily_returns': self.daily_returns,
                'market_value': self.market_value,
                'position': self.positions[pos_key],
                'price': self.prices[pos_key],
                'is_buy': self.is_buy}

    def count_order(self, count, price, pos_key='btc'):
        if not count:
            return
        self.cash = self.cash - count * price
        self.positions[pos_key] = self.positions[pos_key] + count
        self.is_buy = 1 if count else -1
    
    def money_order(self, money, price, pos_key='btc'):
        if not money:
            return
        count = money / price
        self.cash = self.cash - money
        self.positions[pos_key] = self.positions[pos_key] + count
        self.is_buy = 1 if money else -1

    def update_price(self, price, pos_key='btc'):
        if price == self.prices[pos_key] or not self.positions[pos_key]:
            return
        self.prices[pos_key] = price
        now_value = self.market_value
        self.market_value = self.cash + self.positions[pos_key] * price
        self.total_returns = self.market_value / self.starting_cash - 1
        self.daily_returns = self.market_value / self.prev_value - 1
        self.prev_value = now_value
        

class GlobalData(object):

    def __init__(self):
        self._limit_cash = 0.0
        self.order_count = 0
        self.offer_count = 0

    @property
    def limit_cash(self):
        return self._limit_cash

    @limit_cash.setter
    def limit_cash(self, cash):
        self._limit_cash = cash
        self.portfolio = Portfolio(cash)
