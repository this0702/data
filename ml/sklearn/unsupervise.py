#2017.10.19
#帖子推荐，推荐算法
#unicode=utf-8
import os
import sys
from sklearn.feature_extraction.text import CountVectorizer
import scipy as sp
def dist_raw(v1,v2):#计算两个向量之间的欧式距离
    delta=v1-v2
    print(delta)
    return sp.linalg.norm(delta.toarrry())#linalg是sp的线性代数库，norm是用来L2的
#自己新建一个帖子
dir=r'E:\1400OS_03_Codes\data\toy'
posts=[open(os.path.join(dir,f)).read() for f in os.listdir(dir)]#list生成器
vectorizer=CountVectorizer(min_df=1)#int型的时候表示小于1 的不统计，当然也可以写比例
x_train=vectorizer.fit_transform(posts)#这个函数就是提取词，并且做词频统计的
num_samples,num_features=x_train.shape
dist_raw(x_train.getrow(1),x_train.getrow(2))
# print(num_samples,num_features)#5,25表示有5个贴子，25个不同的词
# print(vectorizer.get_feature_names())#这个构造器可以直接返回vectorizer
# print(x_train)#采用的是简单的存储方式

new_post='imaging databases'
new_post_vec=vectorizer.transform([new_post])
# print(new_post_vec.shape)
# print(new_post_vec.toarray())
# print(x_train.getrow(2).toarray())
# print('算距离===========',dist_raw(new_post_vec.toarray(),x_train.getrow(2).toarray()))
#计算所有帖子与新帖子的相似度，推荐出与其相近的帖子
best_i=None
best_dist=sys.maxsize
for i in range(0,num_samples):
    post_vec=x_train.getrow(i)
    d=dist_raw(post_vec,new_post_vec)#加上toarray这个函数，避免raise valueError：dimension mismatch
    print('post=%d with dist=%.2f : %s'%(i,d,posts[i]))
    if(d<best_dist):
        best_dist=d
        best_i=i
best_doc=posts[best_i]

print('best post=%d with dist=%.2f: %s'%(best_i,best_dist,best_doc))





#PART2
import scipy as sp
from sklearn.feature_extraction.text import CountVectorizer
t1='i am a girl and boy'
t2='i am a boy'
vectorizer=CountVectorizer()
t1_vector=vectorizer.fit_transform([t1])
t2_vector=vectorizer.transform([t2])
print((t1_vector-t2_vector).toarray())
#证明了coo-matrix之间是可以进行四则运算的，但是当需要用正常形式的时候比如scipy.linagl.norm(coo-matrix.toarray())