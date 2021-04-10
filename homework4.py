# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:56:00 2021

@author: TiXin
"""


import pandas as pd

pd.set_option('max_columns',None)
#数据加载
dataset=pd.read_csv('./Market_Basket_Optimisation.csv', header=None)
#print(dataset)
#print(dataset.shape) #7501*20

transactions=[]
#按照行进行遍历
for i in range(0,dataset.shape[0]):
    #记录一行Transction
    temp=[]
    #按照列进行遍历
    for j in range(0,dataset.shape[1]):
        if str(dataset.values[i,j]) !='nan':
            temp.append(dataset.values[i,j])
    #print(temp)
    #把这一行的Transction内容计入
    transactions.append(temp)

from efficient_apriori import apriori
itemsets,rules = apriori(transactions, min_support=0.02, min_confidence=0.3)
print('频繁项集：', itemsets)
print('关联规则：', rules)
