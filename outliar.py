#!/usr/bin/env python
# coding: utf-8

## 剔除异常值
## 针对绍兴地区
def outlier(data):
    data['Data1'] = data['Data1'].astype('float32')
    data['Data2'] = data['Data2'].astype('float32')
    data['Diff'] = data['Data1'] - data['Data2']
    ## Data2非空,Data2不能异常
    ## Data1不能异常,二者的差值不能异常    
    data.dropna(subset=['Data1','Data2'],axis=0)
    data1 = data.copy()
    Outlier0 = data[(data['Diff']>40)|(data['Diff']<-12)].index.tolist()
    data.drop(Outlier0,axis=0,inplace=True)
    Outlier1 = data[(data['Data1']>70)|(data['Data1']<-15)].index.tolist()
    data.drop(Outlier1,axis=0,inplace=True)
    Outlier2 = data[data['Data2']==0.00].index.tolist()
    data.drop(Outlier2,axis=0,inplace=True)
    outlier = set(data1.index)-set(data.index)
    outlier = list(outlier)
    outlier = data1.loc[outlier,:]
    del data1
    data = data.reset_index(drop=True)
    data.drop('Diff',axis=1,inplace=True)
    return data,outlier