# private 访问限制
# 果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
# 所以，我们把Student类改一改：

class Student(object):

    def __init__(self, name, score):
        self.__name = name #私有变量
        self.__score = score #私有变量

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
# 如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
class Student(object):
    ...

    #get方法
    def get_name(self):  
        return self.__name

    def get_score(self):
        return self.__score

# 允许外部代码修改score怎么办？可以再给Student类增加set_score方法：

class Student(object):
    ...

    #set方法
    def set_score(self, score):
        self.__score = score

# 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。