import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.image as img
mpl.style.use('classic')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


image_path='matplotlib/lena.png'

im_data=img.imread(image_path)#使用matplotlib仅能对png格式进行读取
print(im_data.shape)

red_data=im_data[:,:,0]
green_data=im_data[:,:,1]
blue_data=im_data[:,:,2]

image1=np.array([blue_data,green_data,red_data])#3 512 512
image1=np.swapaxes(image1,0,1)
image1=np.swapaxes(image1,1,2)

fig=plt.figure()

ax1=plt.subplot2grid(shape=(3,3),loc=(0,0),rowspan=3,colspan=1)
ax1.imshow(im_data)
ax1.set_title('RGB图像')

ax2=plt.subplot2grid(shape=(3,3),loc=(0,1))
ax2.imshow(red_data)
ax2.set_title('R通道图像')

ax3=plt.subplot2grid(shape=(3,3),loc=(1,1))
ax3.imshow(green_data)
ax3.set_title('G通道图像')

ax4=plt.subplot2grid(shape=(3,3),loc=(2,1))
ax4.imshow(blue_data)
ax4.set_title('B通道图像')

ax1=plt.subplot2grid(shape=(3,3),loc=(0,2),rowspan=3,colspan=1)
ax1.imshow(image1)
ax1.set_title('BGR图像')


plt.tight_layout()
plt.show()