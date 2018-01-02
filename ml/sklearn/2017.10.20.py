#数据归一化+帖子推荐
import os
import sys
from sklearn.feature_extraction.text import CountVectorizer
import scipy as sp
import nltk.stem
#对帖子进行回归词干处理,最简单的方法就是重写分析器
english_stemmer=nltk.stem.SnowballStemmer('english')
class StemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer=super(StemmedCountVectorizer,self).build_analyzer()#找到父类，建立去分析器
        return lambda doc:(english_stemmer.stem(w) for w in analyzer(doc))
#计算标准距离
def dist_norm(v1,v2):
    v1_normalized=v1/sp.linalg.norm(v1.toarray())
    v2_normalized=v2/sp.linalg.norm(v2.toarray())
    delta=v1_normalized-v2_normalized
    return sp.linalg.norm(delta.toarray())
DIR=r'E:\1400OS_03_Codes\data\toy'
posts=[(open(os.path.join(DIR,f))).read() for f in os.listdir(DIR)]#读出所有的帖子，并且放到一个列表下
vectorizer=CountVectorizer(min_df=1,stop_words='english')#初始化一个提取特征的对象
x_train=vectorizer.fit_transform(posts)#fit()+transform()自己查文档去必须有fit提取原始文档所有的词语才行
#一下计算新帖子的相似度，以做出推荐（这样的漏洞在于新的帖子的所有词在原生文档中必须得有，否则就报错）
new_post='imaging databases'
new_post_vec=vectorizer.transform([new_post])

best_dist=sys.maxsize
best_i=None
#一下就是一个简单的选出最大的函数了
for i in range(0,x_train.shape[0]):
    curr_dist=dist_norm(new_post_vec,x_train.getrow(i))
    print('post_num=%d,post_content=%s,dist=%.2f'%(i,posts[i],curr_dist))
    if curr_dist<best_dist:
        best_dist=curr_dist
        best_i=i
print('best_post_num=%d,post_content=%s,best_dist=%.2f'%(best_i,posts[best_i],best_dist))

#PART2
#stop_words,删除在任何帖子中都会出现的高频词，这个对帖子相似度区分不大，不应该占用和特定名次一样的权值，直接加在上面
#这样会输出English的常用词
print(sorted(vectorizer.get_stop_words())[0:20])


#PART3
# 近义词权重，image 和 images、information 两个词在上述情况下完全一样权重，显然不合理
#nltk natural language toolkit 自然语言处理在python中常用的包
#处理词干，词干就是指其它的词是由这个词衍生出来的
s=nltk.stem.SnowballStemmer('english')#使用扩展词干处理规则（这个函数决定处理词干的规则）
print(s.stem('tools'))#结果为tool

#PART4
#参数怎么调，不同词的权重应该是不同的，怎么设置
#我们一般认为在本个文件中出现的次数越多，在所有文件中出现的越少，他就越具有代表性
#有公式TF-IDF，在笔记中查看具体式子
from sklearn.feature_extraction.text import TfidfVectorizer#这个是继承于CountVectorizer的，你可以直接用这个算TF-IDF