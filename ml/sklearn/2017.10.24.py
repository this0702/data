#Topic Model主题模型
#LDA狄利克雷
#PART1数据预处理
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
# feature_names=vectorizer.get_feature_names()

#PART2：LDA狄利克雷
from sklearn.decomposition import LatentDirichletAllocation
lda=LatentDirichletAllocation(n_components=30,max_iter=50,learning_method='batch')#学习方法是批量而非online，最大遍历数为50
lda.fit(vectrized)

#PART3：现在已经基本分出类来了，我们可以将各个主题下权重高的词语显示出来
def print_top_word(mode,feature_names,n_top_word):
    for topic_index,components in enumerate(mode.components_):#mode._components输出的是主题-词语矩阵
        print('topic=#%d'%topic_index)
        print(' '.join([feature_names[i] for i in components.argsort()[:-n_top_word-1:-1]]))
    print('主题-词语矩阵:')
    print(mode.components_)
n_top_word=20
print_top_word(lda,vectorizer.get_feature_names(),n_top_word)
#PART4：具体调参