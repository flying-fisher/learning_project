import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('seaborn')  #设置绘图风格
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

Distros= \
[
    'Arch Linux','Ubuntu','Debian','Fedora','Linux Mint','Xubuntu','kubuntu','Gentoo','openSUSE','Other'
]

Colours= \
[
    'b','orange','r','purple','green','chocolate','beige','cyan','magenta','grey'
]
explodes = np.zeros(10)
explodes[1] = 0.1
User = np.array([881, 697, 308, 262, 209, 117, 99, 97, 58, 366])

#默认用法plt.pie(user,labels)
# plt.axis([-1.5,1.5,-1.5,1.5])


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100))
        return '{p:.2f}% ({v:d})'.format(p=pct, v=val)
    return my_autopct


plt.pie(
    User,
    labels=Distros,
    colors=Colours,
    startangle=90,
    shadow=True,
    explode=explodes,
    autopct=make_autopct(User),
    pctdistance=0.8,
    labeldistance=1.1,
    counterclock=True)
#autopct='%2.2f%%'
plt.title('Linux系统份额')
plt.axis('equal')
plt.show()