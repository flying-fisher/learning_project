import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('seaborn')  #设置绘图风格
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

N = 1001
X = np.linspace(-2.0 * np.pi, 2.0 * np.pi, N)
Y = np.random.normal(0, 0.1, N) + np.sin(X)
plt.scatter(
    X,
    Y,
    label='sin曲线散点图',
    marker='s',
    color='red',
    s=10,
    edgecolors='b',
    linewidths=1,
    alpha=0.8)

plt.xlabel('角度')
plt.ylabel('点')
plt.legend()
plt.show()