# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import pyper as pr
import matplotlib.pyplot as plt


data = pd.read_csv('example/k0501.csv')

r = pr.R(use_pandas=True)
r.assign('data1', data)
r('library(lmtest)')
r('fm <- lm(Y ~ X, data=data1)')
print r('summary(fm)')
print r('dwtest(fm)')

fm = r.get('fm$fitted.values')
plt.scatter(data["X"], data["Y"])
plt.plot(data["X"], fm, 'k--')
plt.title('Example5-1')
