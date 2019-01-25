#%%
#导包
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#%%
#设置x,y数据
x=np.linspace(0,2.0*np.pi,101)
y=np.sin(x)
z=np.cos(x)
#%%
xnumber=np.linspace(0,7,15)
ynumber=np.linspace(-1,1,11)
print(xnumber,ynumber)
#%%
# plt.plot(x,y,color='r',label='sin')
# plt.plot(x,z,color='g',label='cos')
plt.plot(x,y,'r',x,z,'g')
plt.xlabel('x轴')
plt.ylabel('y轴')
plt.title('这是一幅图啦')
plt.xticks(xnumber)#设置x的坐标
plt.yticks(ynumber)
plt.grid()#添加格子
plt.legend(['sin','cos'])
plt.axis([0,6.5,-1.1,1.1])#[xstart,xend,ystart,yend]
plt.show()

