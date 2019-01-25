#导包
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import matplotlib as mpl
mpl.style.use('classic')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig1=plt.figure(1)


ax1=plt.subplot2grid(shape=(3,3),loc=(0,0),rowspan=1,colspan=3)
ax1.text(x=0.5,y=0.5,s='图1',va='center',ha='center')

ax2=plt.subplot2grid(shape=(3,3),loc=(1,0),rowspan=1,colspan=2)
ax2.text(x=0.5,y=0.5,s='图2',va='center',ha='center')

ax3=plt.subplot2grid(shape=(3,3),loc=(1,2),rowspan=2,colspan=1)
ax3.text(x=0.5,y=0.5,s='图3',va='center',ha='center')

ax4=plt.subplot2grid(shape=(3,3),loc=(2,0))
ax4.text(x=0.5,y=0.5,s='图4',va='center',ha='center')

ax5=plt.subplot2grid(shape=(3,3),loc=(2,1))
ax5.text(x=0.5,y=0.5,s='图5',va='center',ha='center')

plt.suptitle('网格子图')
plt.tight_layout()
plt.subplots_adjust(top=0.9)
# plt.savefig('matplotlib/result/17.png',format='png',dpi=100)
fig1.show()


fig2=plt.figure(2)
gs1=gs.GridSpec(nrows=3,ncols=3)

ax1=plt.subplot(gs1[0,0:3])
ax1.text(x=0.5,y=0.5,s='图1',va='center',ha='center')

ax2=plt.subplot(gs1[1,0:2])
ax2.text(x=0.5,y=0.5,s='图2',va='center',ha='center')

ax3=plt.subplot(gs1[1:3,2])
ax3.text(x=0.5,y=0.5,s='图3',va='center',ha='center')

ax4=plt.subplot(gs1[2,0])
ax4.text(x=0.5,y=0.5,s='图4',va='center',ha='center')

ax5=plt.subplot(gs1[2,1])
ax5.text(x=0.5,y=0.5,s='图5',va='center',ha='center')

plt.suptitle('使用gridspec')
plt.tight_layout()
plt.subplots_adjust(top=0.9)
# plt.savefig('matplotlib/result/17.png',format='png',dpi=100)
fig2.show()


plt.show()