# InheANDPoly 继承和多态
# 编写了一个名为Animal的class，有一个run()方法可以直接打印：
class Animal(object):
	def run(self):
		print('Animal is running...')
	def eat(self):
		print('Eating meat...')

# 当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：
class Dog(Animal):
    def run(self):
        print('Dog is running...')
	
class Cat(Animal):
    def run(self):
        print('Cat is running...')
# 对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似。
# test
dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()
# cat.eat()当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。