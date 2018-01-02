#type,types
print(type(123))
import types
def fn():
    pass
print(type(fn)==types.FunctionType)#直接利用常量来判断即可
#isInstance
isinstance((1, 2, 3), (list, tuple))
isinstance(b'a', bytes)