#最近邻分类
import numpy as np
#可以有多种算距离的方法
def distance(p0,p1):
    return np.sum((p1-p0)**2)
def nn_classfy(training_set,trianing_lables,new_example):#训练集，标签集，预测集
    ##一般必须进行数据的归一化，方法挺固定的
    training_set-=training_set.mean(axis=0)#-每一列的U
    training_set/=training_set.std(axis=0)#除以标准差
    #new_example来自的集合也需要做这样的变化
    dists=np.array(distance(t,new_example) for t in training_set)#完全支持python中的方法
    nearnest=dists.argmin()#这个方法只有numpy数组可以用，取得下标
    return trianing_lables[nearnest]
