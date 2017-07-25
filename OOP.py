# 面向对象
# 如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象
# 然后，给对象发一个print_score消息，让对象自己把自己的数据打印出来。
class Student(object):

	def __init__(self,name,score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s: %s' % (self.name, self.score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()