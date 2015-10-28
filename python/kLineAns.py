#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果

import pandas as pd
import numpy as np

per_1std = 0.68
per_2std = 0.95

def series_count(flag_list, count):
    import pdb;pdb.set_trace()
    n_now = 1
    n_flag = True
    n_sum = 0
    n_get=0
    for i in xrange(1, len(flag_list[1:])):
        if not n_flag:
            n_flag = True
        elif flag_list[i] != flag_list[i-1]:
            if n_now + 1 == count:
                n_sum += 1
            n_now=1
        else:
            n_now  += 1
            if n_now == count:
                n_get += 1
                n_sum += 1
                n_now = 1
                n_flag = False
        
    return (n_sum, n_get)


k_data = pd.read_csv("./t1000.csv")

vol_data = k_data['volume']
price_data = k_data['close']

vol_desc = vol_data.describe()
price_desc = price_data.describe()
print ("Volume---> mean:%f, std:%f") % (vol_desc['mean'], vol_desc['std'])
print ("Price--->  mean:%f, std:%f") % (price_desc['mean'], price_desc['std'])
#import pdb; pdb.set_trace()
prev_price = price_data.copy()
prev_price = prev_price.shift(1)
prev_price[0] = prev_price[1]

minus_price = price_data - prev_price
minus_price_desc = minus_price.describe()
print ("Minus_price--->mean:%f, std:%f") % (minus_price_desc['mean'], minus_price_desc['std'])

up_count = len(minus_price[minus_price>0].values)
down_count = len(minus_price.values) - up_count
chance = float(up_count)/len(minus_price.values)
print ("Totally %d price UP, and %d price Down, Up chance %f!") % (up_count, down_count, chance)

k_data['minus_price'] = minus_price
k_data['price_flag'] = np.where(minus_price>0,True,False)
price_flag = k_data['price_flag']

k_data['once_same'] = np.where(price_flag==price_flag.shift(),True,False)
one_price_flag = k_data['once_same']
one_same_count = len(one_price_flag[one_price_flag==True].values)
one_diff_count = len(one_price_flag.values) - one_same_count
chance = float(one_same_count)/len(one_price_flag.values)
print ("One same->Totally %d price trend same, and %d price trend diff, price same chance %f!") % (one_same_count, one_diff_count, chance)


#k_data['twice_same'] = np.where(one_price_flag==one_price_flag.shift(),True,False)
#twice_price_flag = k_data['twice_same']
#twice_same_count = len(twice_price_flag[twice_price_flag==True].values)
#if twice_same_count:
#    twice_diff_count = one_same_count - twice_same_count
#    chance = float(twice_same_count)/(twice_same_count + twice_diff_count)
#    print ("Twice same->Totally %d price trend same, and %d price trend diff, price same chance %f!") % (twice_same_count, twice_diff_count, chance)

twice_sum, twice_same_count = series_count(list(price_flag.values), 3)
twice_diff_count=twice_sum - twice_same_count
chance = float(twice_same_count)/twice_sum
print ("Twice same->Totally %d price trend same, and %d price trend diff, price same chance %f!") % (twice_same_count, twice_diff_count, chance)

#k_data['twice_same'] = np.where(one_price_flag==one_price_flag.shift(),True,False)
#twice_price_flag = k_data['twice_same']
#twice_same_count = len(twice_price_flag[twice_price_flag==True].values)
#if twice_same_count:
#    twice_diff_count = one_same_count - twice_same_count
#    chance = float(twice_same_count)/(twice_same_count + twice_diff_count)
#    print ("Twice same->Totally %d price trend same, and %d price trend diff, price same chance %f!") % (twice_same_count, twice_diff_count, chance)

#print (k_data)

