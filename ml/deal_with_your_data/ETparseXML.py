#以下用elementtree来解析xml,比如例子中的post.xml

#part1这种引进xml解析器的方法
# try:
#     import xml.etree.cElementTree
# except ImportError:
#     import xml.etree.ElementTree
    #当然py3已经默认了用哪个c实现ET，so:
import  xml.etree.ElementTree as ET
tree=ET.ElementTree(file='Posts.xml')
root=tree.getroot()#root是一个根元素对象，没有属性(上层节点含有下层节点的所有信息)
for child_root in root:
    print(child_root.tag,child_root.attrib)
#可以看出root其实是一个集合
print(root[0].tag,'\n',root[0].attrib,'\n',root[0].text)
#直接用element自带实现的iter()方法去实现DFS遍历
for elem in tree.iter(tag='something you wanna found'):
    pass


#PART2找到自己想要找的，其中有一些attribute是我不需要的
#支持XPath
for element in tree.iterfind("row[@Id='246']"):#row必须在当前的路径下/Posts/row,row在这里可以直接作为字典
    print(element.tag,element.attrib)

#Part3去构建一个XML文档
###P3.1修改文档，根据上面已有的理念其实很好操作
root[0].set('update','jary')
root[0].attrib['Id']=888
print(root[0].tag,root[0].attrib)#此时只是在内存中有了改变
import sys
# tree.write(sys.stdout)
###p3.2构建一个新的文档
a=ET.Element('elem')
b=ET.SubElement(a,'sub_elem')
b.text='something'
b.attrib={'name':'jary','gender':'man'}
croot=ET.Element('root')
croot.extend((a,))#挂在根节点上,必须传tuple类型
ctree=ET.ElementTree(croot)#构建成一个树对象
ctree.write('sys.stdout')
for child_croot in croot.iter():
    print(child_croot.tag,child_croot.attrib)
print(ctree.getroot()[0][0].attrib)


#Part4，效率分析，可以看出ET方法parseXML也是通过在内存中构建一个树的方法来的，所以不适用于很大的XML文件
