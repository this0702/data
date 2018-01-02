#k均值，聚类帖子的算法
import sklearn.datasets
from sklearn.feature_extraction.text import TfidfVectorizer
#这个是可以计算tf-idf的继承了CountVectorizer的函数
import nltk.stem
english_stemmer=nltk.stem.SnowballStemmer('english')
class StemmedTfidfVectorizer(TfidfVectorizer):
    def build_analyzer(self):
        analyzer=super(TfidfVectorizer,self).build_analyzer()#还是通过CountVectorizer去调用的
        return lambda doc:(english_stemmer.stem(w) for w in analyzer(doc))
MLCOMP_DIR=r'E:\1400OS_03_Codes\data'
#在新闻组进行这个研究
groups = ['comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware',
          'comp.sys.ma c.hardware', 'comp.windows.x', 'sci.space']
#只对train组去研究
trian_data=sklearn.datasets.load_mlcomp('20news-18828','train',mlcomp_root=MLCOMP_DIR,categories=groups)#放MLCOMP的目录，以及文件名
# print(trian_data)
vectorizer=StemmedTfidfVectorizer(min_df=10,max_df=0.5,stop_words='english',decode_error='ignore')
vectrized=vectorizer.fit_transform(trian_data.data)
# num_samples,num_features=vectrized.shape
# print(num_samples,num_features)#3414帖子*4331特征
# print(data.filenames)
# print(len(data.filenames))#一共有18828个帖子
# print(data.target_names)
num_clusters=50#指定K值
from sklearn.cluster import KMeans
km=KMeans(n_clusters=num_clusters,init='random')
km.fit(vectrized)
# print(km.labels_)
#现在km模型被构造好了，怎么用来给新的帖子分到一个合适的簇里呢
new_post='Disk drive problems.Hi,I have a problem with my hard disk.After 1 year it is working only sporadically now.I tried to format it,but now it doesn\'t boot any more'
new_post_vec=vectorizer.transform([new_post])
new_post_label=km.predict(new_post_vec)[0]#这个函数返回的是一个数组,即使只有一个值

