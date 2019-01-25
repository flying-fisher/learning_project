import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('classic')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

n=101
x=np.linspace(0,4.0*np.pi,n)
y1=np.sin(x)
y2=np.cos(x)
y3=y1+y2
y4=y1-y2

fig=plt.figure(figsize=(14,8))

ax1=fig.add_subplot(121)
ax1.plot(x,y3,color='C1',linestyle='--',label='sin+cos')
ax1.set_title('sin+cos')
ax1.set_xlabel('角度',color='r')
ax1.set_ylabel('值',color='r',rotation='horizontal')
ax1.tick_params(axis='x',colors='k')
ax1.tick_params(axis='y',colors='k')
ax1.legend()


ax2=fig.add_subplot(322)
ax2.plot(x,y1,color='C1',linestyle='-',label='sin')
ax2.set_title('sin')
ax2.set_xlabel('角度',color='r')
ax2.set_ylabel('值',color='r',rotation='horizontal')
ax2.tick_params(axis='x',colors='k')
ax2.tick_params(axis='y',colors='k')
ax2.legend()

ax3=fig.add_subplot(324)
ax3.plot(x,y2,color='C1',linestyle='-',label='cos')
ax3.set_title('cos')
ax3.set_xlabel('角度',color='r')
ax3.set_ylabel('值',color='r',rotation='horizontal')
ax3.tick_params(axis='x',colors='k')
ax3.tick_params(axis='y',colors='k')
ax3.legend()


ax4=fig.add_subplot(326)
ax4.plot(x,y4,color='C1',linestyle='-.',label='sin-cos')
ax4.set_title('sin-cos')
ax4.set_xlabel('角度',color='r')
ax4.set_ylabel('值',color='r',rotation='horizontal')
ax4.tick_params(axis='x',colors='k')
ax4.tick_params(axis='y',colors='k')
ax4.legend()

plt.tight_layout()#自动调整各图的间距
plt.subplots_adjust(top=0.92)
fig.suptitle('多子图',fontsize=18)
plt.savefig('matplotlib/result/16.png',format='png',dpi=200)
plt.show()