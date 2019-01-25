#导包
import numpy as np
import matplotlib.pyplot as plt
import matplotlib._color_data as mcd
import matplotlib as mpl
mpl.style.use('seaborn')
# print(mpl.style.available)
#设置x,y
x = np.linspace(-2.0 * np.pi, 2.0 * np.pi, 201)
y = np.sin(x)

#设置轴线
plt.axhline(y=0, color='b', alpha=0.5)
plt.axvline(x=0, color='b', alpha=0.5)

# plt.plot(x,y,color='g',label='sin')
# plt.plot(x,y,color=(0.1,0.2,0.5),label='sin')#rgb
# plt.plot(x,y,color=(183/255,20/255,169/255),label='sin')
# plt.plot(x,y,color=(0.5,0.5,0.5,0.5),label='sin')#RGBA
# plt.plot(x,y,color=(198/255,21/256,198/256),label='sin')

# plt.plot(x,y,color='#c615c6',label='sin')
# plt.plot(x,y,color="0.1",label='sin')#显示灰度值，值越小越黑
# plt.plot(x,y,color=mcd.CSS4_COLORS['chocolate'],label='sin')
# plt.plot(x,y,color='chocolate',label='sin')
# plt.plot(x,y,color='xkcd:navy blue',label='sin')
plt.plot(x, y, color='C1', label='sin')

plt.grid()
plt.legend()
plt.show()
