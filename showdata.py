# -*- coding: utf-8 -*-
"""
 @Time    : 19-3-10 下午6:56
 @Author  : yangzh
 @Email   : 1725457378@qq.com
 @File    : showdata.py
"""
import pandas as pd
import seaborn.apionly as sns
import matplotlib.pyplot as plt

data = pd.read_csv('./logs/people_count_201903101530.csv')

dmap = data['dmap']
time = data['time']
count = data['count']

coun_ = [0,0,0,0,0]
for i in range(len(count)):
    if count[i] < 30:
        coun_[0] += 1
    elif 30 <= count[i] < 33:
        coun_[1] += 1
    elif 33 <= count[i] < 36:
        coun_[2] += 1
    elif 36 <= count[i] < 40:
        coun_[3] += 1
    elif count[i] >= 40:
        coun_[4] += 1
labels = ['low', 'some', 'more some', 'many', 'A ton of']
explode = (0.1, 0, 0, 0, 0)
fig1, ax1 = plt.subplots()
ax1.pie(coun_, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
# ax1.axis('equal')
plt.show()
