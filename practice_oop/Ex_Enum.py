from enum import Enum
Month=Enum('kk',('jan','feb','mon'))
print(Month.__name__)#类名name是kk
print(type(Month))#month是类，而非对象
moth=Month()
print(Month.jan.value)#

class Week(Enum):
    Sun=0
    Mon=1
    Tue=2
print(Week.Sun.value)#拿到枚举值后，通过value取它的值
#判断是对象还是类可以通过type
