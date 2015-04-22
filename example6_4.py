# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import pyper as pr
import matplotlib.pyplot as plt


data = pd.read_csv('example/k0604.csv')

r = pr.R(use_pandas=True)
r.assign('data1', data)

r('library(lmtest)')
r('fm <- lm(YZ ~ XZ, data=data1)')
print r('summary(fm)')
print r('bptest(fm)')

fm = r.get('fm$fitted.values')
plt.scatter(data["XZ"], data["YZ"])
plt.plot(data["XZ"], fm, 'k--')
plt.title('Example6-4')
