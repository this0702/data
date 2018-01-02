#基础的坐标轴使用，如何在图上添加你想要添加的信息等，
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,50)
y1=2*x+1
x0=1
y0=2*x0+1
y2=x**2
plt.figure(num=3,figsize=(8,5))#num表示编号，画板应该在画画之前声明，默认为画板
#将绘画动作返给l1时，注意它返回的是列表
l1,=plt.plot(x,y1,label='line1')
l2,=plt.plot(x,y2,color='red',linestyle='-',linewidth=10.0,label='line2')
#在linspace基础上限制x,y范围
plt.xlim((-1,2))#注意传入tuple
plt.ylim((-2,3))
plt.xlabel('x')
plt.ylabel('y')
#设置刻度（就是设置范围和刻度大小，和上述linspace初始化的工作一致）
#给刻度加上文字描述
plt.yticks([-2, -1.8, -1, 1.22, 3],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
#设置坐标轴,就是边框
ax=plt.gca()#获取边框信息
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#设置轴上的度量写在哪儿
ax.xaxis.set_ticks_position('bottom')#默认为底部
#把left这个轴设置到交叉轴的坐标为0 的地方
ax.spines['left'].set_position(('data',0))#这里有三个参数 data（代表交叉轴坐标信息），outward，axes（表示占交叉轴比例）
ax.spines['bottom'].set_position(('data',0))
#得到一个正常的二维正负图像
#在图中显示信息label(在plot中初始化过)
# plt.legend(loc='upper right')     #一般直接best
#当然单独设置是比较好的
plt.legend(handles=[l1, l2], labels=['up', 'down'],  loc='best')
#图的注释annotate
plt.annotate(r'$2x+1=%s$' % 2, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
#自己查下API：
# 其中参数xycoords='data' 是说基于数据的值来选位置, xytext=(+30, -30) 和 textcoords='offset points' 对于标注位置的描述 和 xy 偏差值,
# arrowprops是对图中箭头类型的一些设置.
plt.text(1,1,'blalbalbala',fontdict={'size': 16, 'color': 'r'})#直接在图里面写字，前面的表示位置
#如果你把线设置的太粗，会遮挡坐标，这个时候用alpha属性
# 把坐标可视度给改一下
for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='red', edgecolor='black', alpha=0.7))
    #bbox设置目的内容的透明度相关参，facecolor调节 box 前景色，edgecolor 设置边框， 本处设置边框为无，alpha设置透明度.
    #bbox把每个坐标看做一个盒子
plt.show()