#!/usr/bin/env python
# coding: utf-8

import numpy as np

def PauTa(arr):
    outlier = []
    for i in range(arr.shape[0]):
        if np.abs(arr[i]-np.mean(arr)) > 1*np.std(arr):
            print(i)
            outlier.append(i) 
    return outlier

