#!/usr/bin/env python
# coding: utf-8
import numpy as np

class Date_Process:
    def __init__(self):
        self.rank_dic = {}

    def time_eda(self,df):
        df['year']      =   df['TaskStartTime'].dt.year
        df['month']     =   df['TaskStartTime'].dt.month
        df['day']       =   df['TaskStartTime'].dt.day
        df['hour']      =   df['TaskStartTime'].dt.hour
        df['day_of_week'] =   df['TaskStartTime'].dt.dayofweek
        return df

    def ranks_fit_transform(self,df):
        df['ranks'] = df['year'] * 400 +  df['month'] * 40 + df['day']

        rank_sort = np.sort(df['ranks'].unique())
        rank_dic = {}
        for i,val in enumerate(rank_sort):
            rank_dic[val] = i
        df['ranks'] = df['ranks'].map(rank_dic)
        self.rank_dic = rank_dic
        return df
