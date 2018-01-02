def fn(self,value):
    print('hello',value)
Hello=type('Hello',(object,),dict(hello=fn))#类名、tuple父类列表、dict是挂上去的函数
h=Hello()
h.hello('python')#动态时直接可以用
class he2(Hello):
    def __call__(self, *args, **kwargs):
        return print(super(he2, self).hello('lisa'))
h2=he2()
h2()
Hello.new_attribute = 'foo'
print(Hello.new_attribute)