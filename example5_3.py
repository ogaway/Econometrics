# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import pyper as pr
import matplotlib.pyplot as plt


data = pd.read_csv('example/k0502.csv')

data_dX = {}
data_dY = {}
for i in data.index:
    if i == 0:
        data_dX[i] = np.nan
        data_dY[i] = np.nan
    if i >= 1:
        data_dX[i] = data["X"][i] - data["X"][i-1]
        data_dY[i] = data["Y"][i] - data["Y"][i-1]
data["dX"] = pd.Series(data_dX)
data["dY"] = pd.Series(data_dY)

r = pr.R(use_pandas =True)
r.assign('data1', data)
r('library(lmtest)')
r('fm <- lm(dY ~ dX, data=data1)')
print r('summary(fm)')
print r('dwtest(fm)')

fm = r.get('fm$fitted.values')
plt.scatter(data["dX"], data["dY"])
plt.plot(data["dX"][1:], fm, 'k')
plt.title('Example5-3')
