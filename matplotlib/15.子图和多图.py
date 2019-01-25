import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

n = 201
x = np.linspace(-2.0 * np.pi, 2.0 * np.pi, n)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = y1 + y2

fig1=plt.figure(1)
plt.subplot(311)
plt.plot(x, y1, color='C1', label='sin',linestyle='--')
plt.legend()
plt.title('sin曲线')
plt.xlabel('角度')
plt.ylabel('值')


plt.subplot(312)
plt.plot(x, y2, color='C2', label='cos',linestyle='-')
plt.legend()
plt.title('cos曲线')
plt.xlabel('角度')
plt.ylabel('值')


plt.subplot(313)
plt.plot(x, y1, color='C3', label='sin+cos',linestyle='-.')
plt.legend()
plt.title('sin+cos曲线')
plt.xlabel('角度')
plt.ylabel('值')


plt.tight_layout()#自动调整间距

fig1.show()

fig2=plt.figure(2)
plt.plot(x, y1, color='C1', label='sin',linestyle='--')
plt.legend()
plt.title('sin曲线')
plt.xlabel('角度')
plt.ylabel('值')
fig2.show()

fig3=plt.figure(3)
plt.plot(x, y2, color='C2', label='cos',linestyle='-')
plt.legend()
plt.title('cos曲线')
plt.xlabel('角度')
plt.ylabel('值')
fig3.show()

fig4=plt.figure(4)
plt.plot(x, y1, color='C3', label='sin+cos',linestyle='-.')
plt.legend()
plt.title('sin+cos曲线')
plt.xlabel('角度')
plt.ylabel('值')
fig4.show()

plt.show()#至少需要一个显示所有的fig1,fig2,...