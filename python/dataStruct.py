#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8


class Portfolio(object):
    def __init__():
        self.starting_cash = 0.0
        self.cash = 0.0
        self.portfolio_value = 0.0
        self.total_returns = 0.0
        self.daily_returns = 0.0
        self.market_value = 0.0
        self.positions = {'btc': 0.0, 'ltc': 0.0}
        self.prices = {'btc': 0.0, 'ltc': 0.0}

    def get_dict():
        return {'starting_cash': self.starting_cash,
                'cash': self.cash,
                'portfolio_value': self.portfolio,
                'total_returns': self.total_returns,
                'daily_returns': self.daily_returns,
                'market_value': self.market_value,
                'positions': self.positions,
                'prices': self.prices}

    def count_order(count, price, pos_key='btc'):
        self.cash = self.cash - count * price
        self.positions[pos_key] = self.positions[pos_key] + count
    
    def money_order(money, price, pos_key='btc'):
        count = money / price
        self.cash = self.cash - money
        self.positions[pos_key] = self.positions[pos_key] + count

    def update_price(price, pos_key='btc'):
        

class GlobalData(object):

    def __init__():
        self._limit_cash = 0.0
        self.portfolio = Portfolio()

    @property
    def limit_cash():
        return self._limit_cash

    @limit_cash.setter
    def limit_cash(cash):
        self._limit_cash = cash
        self.Portfolio.starting_cash = cash
