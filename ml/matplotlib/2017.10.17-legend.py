import matplotlib.pyplot as plt
line1=[1,2,3]
line2=[4,5,6]
line3=[8,8,8]
l1,=plt.plot(line1,label='line1')
l2,=plt.plot(line2,label='line2')
l3,=plt.plot(line3)
l3.set_label('line3')
plt.legend('tak',loc='upper left',ncol=3)
#后面loc这个参数有九宫格的感觉，[upper center lower]+[left right]，直接二元组也是可以的(x,y)
#第二就是这个legend后面接受的是*args,取一个[]，所以用string的话相当于遍历了一下
#其中字典中的ncol代表了这些legend几列

#显然label和legend不是一个东西，label是线的标签，是程序员用的

plt.show()