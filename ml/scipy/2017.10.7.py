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
#为了对数据直观感受，开始绘图
plt.scatter(x,y)#生成散点图
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
#xticks第一个参数是属性的位置，第二个参数是显示的名称1
plt.xticks(
    [w*7*24 for w in range(10)], ['week %i' % w for w in range(10)])#因为x轴本身的刻度是小时
plt.autoscale(tight=True)#自动调节面板的适应规模，很有用，去掉后，图就会空出一大块来
plt.grid(True)#你要格子吗，还有格子的属性也能设置，具体去看看API
# 用scipy建个1阶的模型出来，得到各种参数
fp1,res,a,b,c= sp.polyfit(x,y,1,full=True)
print(fp1,res)
#用参数得到一个模型函数
f1=sp.poly1d(fp1)
#定义一个经验风险函数
def error(f,x,y):
    return sp.sum((f(x)-y)**2)
#计算这个函数将会带来的风险
print(error(f1,x,y))
#画出这条拟合的线
fx=sp.linspace(0,x[-1],1000)#用x生成样本，划分为1000份
plt.plot(fx,f1(fx),linewidth=4,color='red')#定义线的宽度
plt.legend("d=%i"%f1.order,loc='upper left')#显示一些线的信息，比如阶数
fp2,res2,a2,b2,c2= sp.polyfit(x,y,2,full=True)
print(fp2,res2)
#用参数得到一个模型函数
f2=sp.poly1d(fp2)
#定义一个经验风险函数
def error(f,x,y):
    return sp.sum((f(x)-y)**2)
#计算这个函数将会带来的风险
print(error(f2,x,y))
#画出这条拟合的线
fx=sp.linspace(0,x[-1],1000)#用x生成样本，划分为1000份
plt.plot(fx,f2(fx),linewidth=4,color='yellow')#定义线的宽度
plt.legend("d=1",loc='upper left')
plt.legend("d=2",loc='upper left')
plt.legend("d=0",loc='upper left')
plt.show()#跑出散图来点
#plt是画板，可以得到很多的图，然后统一show出来

#比对之后显然是模型2好，并且也不存在过度拟合啥的，怎么用这个模型呢
print(f2)
#估计以下达到100000访问量的时候的周数
from scipy.optimize import fsolve
reached_max=fsolve(f2-100000,800)/(7*24)#从第800小时开始算就行了
print('第%f周将会达到100000访问量'%reached_max)

