from matplotlib import pyplot as plt
from sklearn.datasets import load_iris#这就是sklearn的方便之处之一，这个库里还默认的集成了很多数据
import numpy as np
data=load_iris()
features=data['data']#data是一个字典
feature_name=data['feature_names']
target=data['target']
labels=data['target_names'][data['target']]#target_names可以看为labels
# print(data['target_names'])#['setosa' 'versicolor' 'virginica']标签名称
# print(feature_name)#特征名称4种
# print(features)#features是一个二维数组,numpy
# print(target)#预测结果三种
for t,c,m in zip(range(3),'RGB','>ox'):
    plt.scatter(features[target == t,0],features[target == t,1],c=c,marker=m)
plt.legend('012')
plt.xlabel(feature_name[0])
plt.ylabel(feature_name[1])
#通过观察，判断setosa可以通过petal的长度判断
plength=features[:,2]#0,1,2,3输出第3列,每行的标签还在
#去出这一列里面是setosa的最大值，和不是它的最小值，看图
setosa_p_max=plength[target==0].max()
non_setosa_p_min=plength[target!=0].min()
#直接通过这个长度去判断是不是setosa,也是不对的，应该简单的做个模型，小于2就行了
if(features[:,2].any()<2):
    print('is_setosa')
print(features.shape)
# plt.show()
#接下来通过算法构建第一个简单的分类器,具体分析就不写了
#分类简单的分virginica和为非virginica
is_vir=(labels=='virginica')
best_acc=-0.1
#针对所有特征的,所有的阈值进行一一检验建模二重循环
for clm in range(features.shape[1]):
    thresh=features[:,clm].copy()
    thresh.sort()#从小到大排序
    for t in thresh:
        pre=(features[:,clm]>t)
        acc=(pre==is_vir).mean()
        if acc>best_acc:
            best_acc=acc#最佳准确率
            best_clm=clm#最佳的特征
            best_t=t#最佳的阀值
print('best_acc=%f,best_clm=%d,best_t=%f'%(best_acc,best_clm,best_t))
#这样就得到了哪个特征值，在哪个值得情况下可以最优的区分出vir来
