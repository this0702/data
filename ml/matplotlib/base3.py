#柱状图-bar，和生成符合均匀分布的图
import matplotlib.pyplot as plt
import numpy as np
n = 12
X = np.arange(n)
Y1= (1 - X / float(n))*np.random.uniform(0.5, 1.0, n)
Y2= (1 - X / float(n))*np.random.uniform(0.5, 1.0, n)#1~12符合0.5~1.0之间的概率
plt.bar(X,Y1,facecolor='#9999ff',edgecolor='white')
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')#这两种颜色都挺漂亮
#ha横向居中，va纵向底部对齐
for x, y in zip(X, Y1):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x, y+0.01, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x ,-y-0.01, '%.2f' % y, ha='center', va='top')
plt.show()
