# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import pyper as pr
import matplotlib.pyplot as plt


data = pd.read_csv('example/k0602.csv')
data["lnX"] = np.log(data["X"])
data["lnY"] = np.log(data["Y"])

r = pr.R(use_pandas=True)
r.assign('data1', data)

r('library(lmtest)')
r('fm <- lm(lnY ~ lnX, data=data1)')
print r('summary(fm)')
print r('bptest(fm)')

fm = r.get('fm$fitted.values')
plt.scatter(data["lnX"], data["lnY"])
plt.plot(data["lnX"], fm, 'k--')
plt.title('Example6-3')
