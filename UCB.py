#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 07:50:19 2019

@author: rupesh
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math


dataset = pd.read_csv('Ads_CTR_Optimisation.csv')


N = 10000
d = 10
number_of_selections = [0] *d
sum_of_rewards = [0] * d
total_reward = 0
ads_selected = []

for n in range(0, N):
    ad = 0
    max_upperbound = 0
    for i in range(0,d):
        if number_of_selections[i] > 0 :
            average_reward  = sum_of_rewards[i] / number_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n+1) / number_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upperbound:
            max_upperbound = upper_bound
            ad = i
    ads_selected.append(ad)
    number_of_selections[ad] = number_of_selections[ad] + 1
    reward = dataset.values[n,ad]
    sum_of_rewards[ad] =  sum_of_rewards[ad] + reward
    total_reward = total_reward + reward



plt.hist(ads_selected)
plt.title('Histogram of Ad Selection')
plt.xlabel('Ads')
plt.ylabel('Number_of_times_each_ad_was_selected')
plt.show()