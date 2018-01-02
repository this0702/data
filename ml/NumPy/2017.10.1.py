#encoding=utf-8
import scipy as sp
import matplotlib.pyplot as plt
###1.数据处理
#返回一个numpy.array
data=sp.genfromtxt(r'E:\python_code\ml\1400OS_01_Codes\data\web_traffic.tsv',delimiter='\t')
print(data[0:10])
print(data.shape)
#索引标记
x=data[:,0]
y=data[:,1]
#y的无效值总数
print(sp.sum(sp.isnan(y)))
#8:743,无效值直接清理掉,注意array可以直接作为索引
x=x[~sp.isnan(y)]
y=y[~sp.isnan(y)]
#为了对数据直观感受
plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks(
    [w * 7 * 24 for w in range(10)], ['week %i' % w for w in range(10)])
plt.autoscale(True)
plt.grid(True)
plt.show()
