# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:35:38 2021

@author: TiXin
"""


from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np
#第一步：数据加载，数据中有仲文要加encoding
data =pd.read_csv('car_data.csv', encoding='gbk')
#print(data)
#训练集
train_x=data[['人均GDP','城镇人口比重','交通工具消费价格指数','百户拥有汽车量']]
#print(train_x)
'''
#把数据数字化，如果有非数字的，one-hot或LabelEncoder
from sklearnpreparocessing import LabelEncoder
le= LabelEncoder()
train_x['Gender']=le.fit_transform(train_x['Gender'])
'''
#数据规范化到【0，1】空间
min_max_scaler=preprocessing.MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x)
pd.DataFrame(train_x).to_csv('temp.csv',index=False)
#print(train_x)
'''
#kmEANS手肘法：统计不同K取值的误差平方和
import matplotlib.pyplot as plt
sse=[]
for k in range(1,11):
    #KMeans 算法
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(train_x)
    sse.append(kmeans.inertia_)
x=range(1,11)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x,sse,'o-')
plt.show()
#拐点在K=4
'''

# 使用KMeans聚类
kmeans=KMeans(n_clusters=4)
#kmeans.fit(train_x)可以先fit再predict 或者同时进行
predict_y=kmeans.fit_predict(train_x)
#合并聚类结果，插入到原数据中
result=pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类结果'},axis=1,inplace=True)
print(result)
#将结果保存到CSV文件中
result.to_csv('customer_cluster_result.csv',index=False)

#使用层次聚类
from scipy.cluster.hierarchy import dendrogram,ward
from sklearn.cluster import KMeans, AgglomerativeClustering
import matplotlib.pyplot as plt
model = AgglomerativeClustering(linkage='ward',n_clusters=4)
y=model.fit_predict(train_x)
print(y)

linkage_matrix = ward(train_x)
dendrogram(linkage_matrix)
plt.show