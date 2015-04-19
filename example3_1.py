# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import pyper as pr
import matplotlib.pyplot as plt

"""
テキスト第3章「単純回帰分析」における例題3.1のPythonコードです。
「k031.csv」ファイルはテキスト付属データセットです。
各自で出版社サイトよりダウンロードしてください。
---
fm <- lm(Y ~ X, data=data1)
でRを使って単純回帰分析をしてくれる。
Pythonでも回帰分析してくれるコマンドはあるようだが、
情報量や分析ツールの多さはRの方が優れる部分が多いとか。
PypeRを使えばそういうRのメリットもPythonで引き継ぐことが出来そうですね。
---
"""

# データ読み込み
data = pd.read_csv('k031.csv')

# Rへデータ渡す
r = pr.R(use_pandas =True)

# Rのコマンド実行
r.assign('data1', data)
print r('summary(data1)')
r('fm <- lm(Y ~ X, data=data1)')
print r('summary(fm)')

#Python側にとってくる
fm = r.get('fm$fitted.values')
#散布図、回帰直線を描く
plt.scatter(data["X"], data["Y"])
plt.plot(data["X"], fm, 'k--')
plt.title('PypeR Sample')
