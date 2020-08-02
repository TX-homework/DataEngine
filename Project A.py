# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 20:58:12 2020

@author: TiXin
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
    
# 请求URL
base_url= 'http://car.bitauto.com/xuanchegongju/?l=8&mid=8'
# 得到页面的内容
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
html=requests.get(base_url,headers=headers,timeout=10)
content = html.text
# 通过content创建BeautifulSoup对象
soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
#抓取搜索出的内容
temp = soup.find('div',class_="search-result-list")
#建立最终输出的信息列名
df=pd.DataFrame(columns=['car','lowest_price(万)','highest_price(万)','image_link'])
#抓取每个车型对应的块
item_list=temp.find_all('div',class_="search-result-list-item")
#print(item_list)
#抓取块里的具体内容
for item in item_list:
    temp={}
    car=item.find(class_='cx-name text-hover').text
    #print(car)
    price=item.find(class_='cx-price').text
    if price == '暂无':
        lowest_price='暂无'
        highest_price='暂无'
    elif '-' in price:
        lowest_price=float(price.split('-')[0])
        highest_price=float(price.split('-')[1][:-1])
    else:
        lowest_price=float(price[:-1])
        highest_price=float(price[:-1])
    #print(lowest_price)
    #print(highest_price)
    image_link= 'http'+item.find('img').get('src')
    #print(image_link)
    #把抓取到的信息赋给相应的列
    temp['car'],temp['lowest_price(万)'],temp['highest_price(万)'],temp['image_link']=car,lowest_price,highest_price,image_link
    df = df.append(temp,ignore_index=True)
print(df)
#输出csv格式文件
df.to_csv('VW_SUV_info.csv',index=False,encoding='gbk')
