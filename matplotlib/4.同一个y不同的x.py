#%%
#导包
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

#%%
#设置x,y数据
y = np.linspace(0, 2.0 * np.pi, 101)
x1 = np.sin(y)
x2 = np.sinh(y)

ynumber = np.linspace(0, 7, 15)
xnumber1 = np.linspace(-1, 1, 11)
xnumber2 = np.linspace(0, 300, 11)

figure, ax1 = plt.subplots()
ax2 = ax1.twiny()

pic1, = ax1.plot(x1, y, color='r', label='sin')
pic2, = ax2.plot(x2, y, color='b', label='sinh')
pics=[pic1,pic2]

ax1.legend(pics,[pic.get_label() for pic in pics ])#也行的
# ax2.legend(pics,[pic.get_label() for pic in pics ])

ax1.set_xlabel("计算值",color=pic1.get_color())
# ax2.set_xlabel('角度/值',color=pic2.get_color())#ax2不具有对color,grid,label的控制权
ax2.set_xlabel('计算值',color=pic2.get_color())
ax1.set_ylabel('角度值',color=pic2.get_color())
#设置y轴颜色
ax1.tick_params(axis='x',colors=pic1.get_color())
ax2.tick_params(axis='x',colors=pic2.get_color())
#设置x轴的颜色
ax1.tick_params(axis='y',colors='k')

#设置x轴的间隔
ax1.set_yticks(ynumber)

#设置y轴的间隔
ax1.set_xticks(xnumber1)
ax2.set_xticks(xnumber2)

ax1.grid(color=pic1.get_color(),linestyle='--')
ax2.grid(color=pic2.get_color(),linestyle='--')
ax1.xaxis.grid(False)
# ax2.yaxis.grid(False)
# ax1.xaxis.grid(False)
ax1.set_title('图')

# plt.title('这是一幅图啦')

plt.show()
