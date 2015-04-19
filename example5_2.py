# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import pyper as pr
import matplotlib.pyplot as plt

"""
テキスト第5章「自己相関」における例題5.2のPythonコードです。
「k0502.csv」ファイルはテキスト付属データセットです。
各自で出版社サイトよりダウンロードしてください。
---
library(lmtest)で「lmtest」というライブラリをインポートしてから、
dwtest()でダービン＝ワトソン統計量による自己相関の有無の仮説検定を行う。
また、あらかじめ「lmtest」はRでインストールしておかなければPypeRでもこのコマンドは動きません。
Rstudioを開き、Tools -> Install Packages で開かれた画面の
Packagesに「lmtest」と入力してInstallボタンをクリックすればインストールされるはず。
---
"""

# データ読み込み
data = pd.read_csv('Econometrics/example/k0502.csv')

# Rへデータ渡す
r = pr.R(use_pandas =True)

# Rのコマンド実行i,X,Y
r.assign('data1', data)
print r('summary(data1)')
r('library(lmtest)')
r('fm <- lm(Y ~ X, data=data1)')
print r('summary(fm)')
print r('dwtest(fm)')

#Python側にとってくる
fm = r.get('fm$fitted.values')
#散布図、回帰直線を描く
plt.scatter(data["X"], data["Y"])
plt.plot(data["X"], fm, 'k--')
plt.title('Auto Correlation')
