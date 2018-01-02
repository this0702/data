#自己做的ORM，就是一个类对应一个数据库表，一个对象对应表中一行
#测试：
# class User(Model):
#     # 定义类的属性到列的映射：
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')
#
# # 创建一个实例：
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# # 保存到数据库：
# u.save()
L=['1','2','3']
print(','.join(L))#注意这个join的特殊用法