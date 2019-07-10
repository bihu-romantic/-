#!/usr/bin/env python
# coding: utf-8

def engineering(data):
    ## 相位
    Phase = []
    for i in data['DeviceName'].values:
        if 'A相' in i:
            Phase.append('A相')
        elif 'B相' in i:
            Phase.append('B相')
        elif 'C相' in i:
            Phase.append('C相')
        else:
            Phase.append(-1)
    data['Phase'] = Phase

    ## 替换A相，B相，C相
    data['DeviceName_Phase'] = data['DeviceName']
    for i, num in enumerate(data['DeviceName_Phase'].values):
        if 'A相' in num:
            data.loc[i, 'DeviceName_Phase'] = data.loc[i, 'DeviceName_Phase'].replace('A相', '')
        if 'B相' in num:
            data.loc[i, 'DeviceName_Phase'] = data.loc[i, 'DeviceName_Phase'].replace('B相', '')
        if 'C相' in num:
            data.loc[i, 'DeviceName_Phase'] = data.loc[i, 'DeviceName_Phase'].replace('C相', '')
    return data