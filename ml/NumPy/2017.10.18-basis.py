#specific document：https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
import  numpy as np
#一.array creation
a=np.array([[[1,2,3],[1,2,3]],[[2,2,2],[3,3,3]]])
print(a.ndim)
print(a.shape)#(a,b,c)==(n,m,nidm)n*m是秩为3的时候的行*列
#1.aotu 1D creation
b=np.arange(0,100,5)#范围加步长
c=np.linspace(0,100,10)#范围加个数
#2.Muti_D的初始化办法
d=np.ones((2,3,4),dtype=int)#np.zero(),np.empty....,其中的tuple是生成的shape
e=np.arange(1000).reshape((5,10,20))#最常用的
#二.basic operate

#1.矩阵四则运算：numpy数组的四则运算针对每个元素so:
x=np.array([[1,2],[3,4]])
y=np.array([[0,1],[1,0]])
print(x*y)#代表的并非点乘
print(x.dot(y))#点乘
#2.关于axis直接到本文参考中去搜例子

#三slice,iterator
# 1.iterator
for ee in e:
    print(ee)
for eee in e.flat:#将数组中每个数都输出
    print(eee)



