#导包
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('classic')
#设置参数
mean=100
st=15
N=1000
binsize=20
IQ=np.random.normal(mean,st,N)
counts,bins,_ =plt.hist(IQ,binsize,facecolor='C4',label='IQs',normed=False)
print('bins:',bins)
print(bins.shape)
print('counts:',counts)
print(counts.shape)

plt.plot(bins[1:] ,counts,label='series',color='C2')#bins比counts多一个，所以[1:]
plt.xlabel('IQ')
plt.ylabel('Count')
plt.xticks(bins)
plt.grid()
plt.legend()
plt.show()
