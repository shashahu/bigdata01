# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 15:42:28 2018

@author: lenovo
"""

weather={
        "未来五天的天气":["15℃","27℃","25℃","28℃","24℃"],
        "未来五天的情况":["小雨","晴朗","晴朗","晴朗","多云"],
        '今天星期几':["星期一","星期二","星期三","星期四","星期五"]}
print(len(weather["今天星期几"]))
print(max(weather["未来五天的天气"]))
for i in range(len(weather["今天星期几"])):
    print("今天"+weather['今天星期几'][i]+"天气"+weather['未来五天的情况'][i])