# ClassANDInstance
# 类和实例
# Python中，定义类是通过class关键字：
class Student1(object):
	pass
# class后面紧接着是类名，即Student，类名通常是大写开头的单词
# 紧接着是(object)，表示该类是从哪个类继承下来
# 继承的概念我们后面再讲，通常，如果没有合适的继承类
# 就使用object类，这是所有类最终都会继承的类。

# 定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的：
bart1 = Student1()
bart1.name = 'Bart Simpson'

# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
class Student2(object):
	def __init__(self,name,score):
		self.name = name 
		self.score = score

# 注意：特殊方法“init”前后有两个下划线！！！
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身
# 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了
# 必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
bart2 = Student2('Bart Simpson', 59)
print("姓名",bart2.name)
print("成绩",bart2.score)

# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self
# 并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别
# 所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

# 数据封装

# 面向对象编程的一个重要特点就是数据封装。
# 在上面的Student类中，每个实例就拥有各自的name和score这些数据。
# 我们可以通过函数来访问这些数据，比如打印一个学生的成绩：
# 既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问
# 可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。
# 这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：
class Student3(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

# 要定义一个方法，除了第一个参数是self外，其他和普通函数一样。
# 要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入：
bart3 = Student3('Nicolo', 99)
bart3.print_score()