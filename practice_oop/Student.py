# #定义一个student对象
# class Student(object):#class 类名(父类名称)#最高级的是object
#     def __init__(self,name,score):#self表是你声明的该对象
#         self.name=name
#         self.score=score
#     def getScore(self):#必须传入这个实际的对象
#         return self.score
#
# stu1=Student('jary',100)
# print(stu1.getScore())
# #当然与java不同处在于这个对象的传入参数,可以在外面直接挂上去
# class Car(object):
#     print('carcar')
# Car.name='this'
# print(Car.name)

# # 一般情况下，定义个类的目的就是要封装下，外部随意A.B访问就没有意义了。
# #python中用__name表示
# class Student(object):#class 类名(父类名称)#最高级的是object
#     def __init__(self,name):#,score):#self表是你声明的该对象
#         self.__name=name
#         # self.__score=score#只在当前类可以取得
#     def getScore(self):#必须传入这个实际的对象
#         return self.__score
#     def setScore(self,score):
#         if 0<=self.__score<=100:#注意python中这个可以比较大小的用法
#             self.__score=score
#         else:
#             raise ValueError('bad score')
# #即使是私有的你也可以在外部调用
# # stu=Student('jary',120) #初始化可以通过，因为初始化语句没有校验
# stu1=Student('lisa')
# stu1.setScore(120)#只有直接设值才会用到校验
# # print(stu1._Student__name)
# print(stu1.getScore())
# # print(stu1._Student__name)

##与下面加了装饰器的对比这种方式
# class Student(object):
#
#     def get_score(self):
#          return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
# Stu1=Student()
# Stu1.set_score(1000)

#使用装饰器@property实现getter/setter
class Student(object):
    def __call__(self, *args, **kwargs):
        print('有了call方法后，可以直接通过对象名调用这个方法，也就是对象和函数基本没有区别了')
        print(args,kwargs)
    def __getattr__(self, item):
        if item=='name':
            return 'everyone'
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)#这样就可以调试你想用的属性
    @property
    def score(self):
         return self.__score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value
    def __str__(self):#用户看得类信息（直接print时）
        return r'his/her/n score is %d '%self.__score#注意这儿这个r的用法
    __repr__=__str__

stu1=Student()
stu1.score=60
print(stu1.score)#加了装饰器，方法可以直接当做属性来用
print(Student)
print(stu1)
print(stu1.name)
# print(stu1.age)#这个会报错
print(stu1(['我','很','弱','要','多','问'],{1:'别'}))#这个实例直接传参当成函数用了


