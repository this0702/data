#散点图，以及随机生成服从正态分布概率的数据
import matplotlib.pyplot as plt
import numpy as np
n=1024
X=np.random.normal(0,1,n)#每一个点的x值
Y=np.random.normal(0,1,n)
T=np.arctan2(Y,X)#就是tan(y/x),可以处理x为0的情况，也就是根据原点到(x,y)点的射线方向来决定颜色
plt.scatter(X, Y, s=75, c=T, alpha=.5)
plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
#忽略刻度
plt.xticks(())
plt.yticks(())
plt.show()