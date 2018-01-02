# kaggle竞赛入门，泰坦尼克号，逻辑回归
# 1.初步了解数据-panda #dataframe
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import seaborn as sns

plt.style.use('ggplot')
sns.set_style('white')
pylab.rcParams['figure.figsize'] = 8, 6

data_train = pd.read_csv('../data_set/train.csv')  # 读入dataform的数据


# 展示数据更多的细节，并且封装为dataform显示
def describe_more(df):
    # 注意作者在这里用的同行加分号的形式，也是可以的，不符合pep8规范
    var = []
    l = []
    t = []
    for x in df:
        var.append(x)
        l.append(len(pd.value_counts(df[x])))
        t.append(df[x].dtypes)
    levels = pd.DataFrame({'Variable': var, 'Levels': l, 'Datatype': t})
    levels.sort_values(by='Levels', inplace=True)
    return levels


# 这个函数真的很棒bar
#利用矩阵条的高度反映数值变量的集中趋势，以及使用 errorbar 功能（差棒图）来估计变量之间的差值统计。
# 请谨记 bar plot 展示的是某种变量分布的平均值，当需要精确观察每类变量的分布趋势，boxplot 与 violinplot 往往是更好的选择
def plot_categories(df, cat, target, **kwargs):
    row = kwargs.get('row', None)
    col = kwargs.get('col', None)
    facet = sns.FacetGrid(df, row=row, col=col)
    facet.map(sns.barplot, cat, target)
    facet.add_legend()
    plt.show()


# seaborn建立matplotlib上的一个figure中显示多个图基础上，以将结构直接链接到数据集结构上进行绘制
# col,row对应的是大图（而不是子图的），hue对应的是第三维
def plot_distribution(df, var, target, **kwargs):
    row = kwargs.get('row', None)  # sns的列
    col = kwargs.get('col', None)
    facet = sns.FacetGrid(df, hue=target, aspect=4, row=row, col=col)
    # 这个函数先画好大图结构
    # df是数据
    # hue是第三维，不同维度用不同的线显示
    # aspect是横轴：纵轴=4:1
    # row,col
    facet.map(sns.kdeplot, var, shade=True)
    # 这个函数具体画小图，小图row=var，折线图
    facet.set(xlim=(0, df[var].max()))
    # 设置x轴范围
    facet.add_legend()
    plt.show()


# 画相关关系热图的
def plot_correlation_map(df):
    corr = data_train.corr()  # 直接分析相关性
    _, ax = plt.subplots(figsize=(16, 12))  # 返回一个figure对象和ax对象
    cmap = sns.diverging_palette(220, 10, as_cmap=True, center='light')  # 这个函数会生成一个色盘或者一个map盘，当as_cmap为true的时候
    _ = sns.heatmap(
        corr,  # data
        cmap=cmap,  # 色盘
        square=True,  #
        cbar_kws={'shrink': .9},  # colorbar，默认显示，这个是它的一些信息，缩小到0.9倍
        ax=ax,  # 提供subplots出的面板的轴信息
        annot=True,  # 将数值写在热图的各个点上1
        annot_kws={'fontsize': 12},  # 字体大小
        center=0,  # 设置中心为0，最凉
        vmin=-1,
        vmax=1
    )
    plt.show()


# 1.初步分析总体
print(data_train.head(5))  # or tail()
data_train.info()  # 可能有缺失数据
# 对数据有直观的印象
print(describe_more(data_train))  # 这个是个很棒的函数
data_train.describe()

# 2.matplotlib用图认识数据
# plot_correlation_map(data_train)#数据间相关关系热图，第一步
# plot_distribution( data_train , var = 'Age' , target = 'Survived' , row = 'Sex' )#关于年龄的不同性别的，存活人数，和没存活人数
# 重合部分很多的属性不适合用来区分数据
# 下来分析一下fare和survive的关系
# plot_distribution(data_train,var='Fare',target='Survived',row='Sex')
# plot_histograms(data_train, variables=data_train.items,n_cols=1,n_rows=1)
plot_categories(data_train, cat='Embarked', target='Survived')

print(describe_more(data_train))
