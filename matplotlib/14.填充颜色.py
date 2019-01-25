import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False



x = np.linspace(-2.0 * np.pi, 2.0 * np.pi, 201)
c, s = np.cos(x), np.sin(x)
plt.plot(x,s,color='r',label='sin')
plt.plot(x,c,color='g',label='cos')
# plt.fill_between(x,0,s,color='C3')#显示sin曲线和y=0围成的面积
#fill_between(x, y1, y2=0, where=None, interpolate=False)
plt.fill_between(x,c,s,where=(c>=s),interpolate=True,color='C1',alpha=0.5)
plt.fill_between(x,c,s,where=(c<=s),interpolate=True,color='C2',alpha=0.5)
plt.fill_between(x[20:43],c[20:43],s[20:43],color='C6')

plt.legend()
plt.title('填充图')
plt.show()
