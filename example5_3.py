# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import pyper as pr
import matplotlib.pyplot as plt

"""
テキスト第5章「自己相関」における例題5.3のPythonコードです。
「k0502.csv」ファイルはテキスト付属データセットです。
各自で出版社サイトよりダウンロードしてください。
---
本書では「k0502.csvのファイル」をExcelで予め計算して、
dX,dYを求めたものを「k0503.csv」として保存し、
「k0503.csv」を使ってRで回帰分析を行っていますが、
せっかくなのでExcelを使わずにデータ加工の部分もpandasを使ってPythonにやらせます。
Rだとデータ加工がしづらいと言われますが（やったことないからわからないけど）、
Pythonだと簡単に出来るので特有のメリットと言えそうですね。
---
"""
# データ読み込み
data = pd.read_csv('Econometrics/example/k0502.csv')

#データ加工
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

# Rへデータ渡す
r = pr.R(use_pandas =True)

# Rのコマンド実行i,X,Y
r.assign('data1', data)
r('library(lmtest)')
r('fm <- lm(dY ~ dX, data=data1)')
print r('summary(fm)')
print r('dwtest(fm)')

#Python側にとってくる
fm = r.get('fm$fitted.values')

#散布図、回帰直線を描く
plt.scatter(data["dX"], data["dY"])
plt.plot(data["dX"][1:], fm, 'k')
plt.title('Example5-3')
