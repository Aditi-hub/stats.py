# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:17:01 2019

@author: Aditi
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats



import pandas as pd
var=pd.read_csv("sunspots.csv")
print('Mean: ',var['Sunspots'].mean())
print('Meadian: ',var['Sunspots'].median())
print('Variance: ',var['Sunspots'].var())

h=np.asarray(var['Sunspots'].dropna())
h=sorted(h)

fit=stats.norm.pdf(h,np.mean(h),np.std(h))

plt.plot(h,fit,'-',linewidth=2)
plt.hist(h,normed=True,bins=100)
plt.show()


print('Skew: ',var['Sunspots'].skew())
print('Kurtosis: ',var['Sunspots'].kurt())
