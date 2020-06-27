# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 09:59:30 2020

@author: TiXin
"""

# Action 1

import numpy as np
a= np.arange(2,101,2)
b= np.sum(a)
print (a) 
print(b)

# 返回2550

# Action 2

from pandas import Series, DataFrame
data={'Chinese':[68,95,98,90,80],'Math':[65,76,86,88,90],'English':[30,98,88,77,90]}
df=DataFrame(data, index=['张飞','关羽','刘备','典韦','许褚'],columns=['Chinese','Math','English'])
#修改各列的名称
df=df.rename(columns={'Chinese':'语文','Math':'数学','English':'英语'})
#输出各种统计
result={'平均分数':[df.mean()],'最小分数':[df.min()],'最大成绩':[df.max()],'方差':[df.var()],'标准差':[df.std()]}
print(result)
'''
df.loc['Row_sum'] = df.apply(lambda x: x.sum())
'''
#计算每个行的总成绩，其实我还没看懂下面这一行的代码，是不是定义了一个行数，逐列求和？
df['Col_sum'] = df.apply(lambda x: x.sum(), axis=1)
df=df.sort_values('Col_sum', ascending=False)
print(df)

# Action 3
from pandas import DataFrame
import pandas as pd
result=pd.read_csv('car_complain.csv')
result=result.drop('problem',1).join(result.problem.str.get_dummies(','))
#print(result.columns)
#问题：不明白此处get_dummies的用法，一般不应该是把要分割的列放在括号内吗？
#取第七列以后的数据,从第八列开始
tags=result.columns[7:]
#print(tags)
df=result.groupby(['brand'])['id'].agg(['count'])
df2=result.groupby(['brand'])[tags].agg(['sum'])
#把投诉总数和不同类型problem总数放在同一个dataframe里面
df2=df.merge(df2,left_index=True, right_index=True,how='left')
#将dataframe groupby类型重新转换为dataframe
df2.reset_index(inplace=True)
df2=df2.sort_values('count',ascending=False)
print('投诉总数排行')
print(df2)
query=('A11','sum')
df2=df2.sort_values(query,ascending=False)
print('A11投诉排行')
print(df2)

