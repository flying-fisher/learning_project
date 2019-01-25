import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlp
mlp.style.use('seaborn-ticks')#选择不同的显示方式
print(mlp.style.available)
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

x=np.linspace(-2.0*np.pi,2.0*np.pi,201)
y=np.sin(x)
z=np.cos(x)

plt.plot(x,y,'r',label='sin')
plt.plot(x,z,'g',label='cos')

plt.axes().spines['bottom'].set_position(('data',0))
plt.axes().spines['left'].set_position(('data',0))

plt.axhline(y=plt.ylim()[0],color='k',alpha=1)#alpha 控制颜色的多少分之一
plt.axvline(x=plt.xlim()[0],color='k')

plt.title('sin和cos的曲线图')
# plt.xlabel('角度')
# plt.ylabel('值')
plt.legend()
plt.grid()


plt.show()