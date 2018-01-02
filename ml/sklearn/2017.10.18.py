from matplotlib import pyplot as plt
from sklearn.datasets import load_iris#这就是sklearn的方便之处之一，这个库里还默认的集成了很多数据
import numpy as np
data=load_iris()
features=data['data']#data是一个字典
feature_name=data['feature_names']
target=data['target']
# print(data['target_names'])
# print(feature_name)#特征名称4种
# print(features)#features是一个二维数组,numpy
# print(target)#预测结果三种
for t,c,m in zip(range(2),'RG','ox'):
    plt.scatter(features[target == t,1],features[target == t,2],c=c,marker=m)
plt.legend('012')
plt.xlabel(feature_name[1])
plt.ylabel(feature_name[2])
plt.show()