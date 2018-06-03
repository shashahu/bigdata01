# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:49:53 2018

@author: lenovo
"""
import json
import urllib.request as r
city=input("请输入城市的拼音:")
address='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address.format(city)).read().decode('utf-8','ignore')
print(info)
data=json.loads(info)

#print('id'+str(data["weather"][0]['id'])+"\n最高温度"+str(data["main"]['temp_max'])+'\n气压'+str(data["main"]['pressure']))