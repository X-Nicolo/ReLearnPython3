# 定义注册函数
def enroll(name,gender,age,city):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)

enroll("Nicolo","male",24,"Xian")

#或定义某几个参数
def enroll2(name,gender,age= 24,city = "Xian"):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)
enroll2("Nicolo","male")

#可变参数
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum +n
	return sum

#test
print("1-2之和：",calc(1,2))

# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
nums = [1,2,3,4,5,6,7,8,9,10]
print("1-10之和：",calc(*nums))
# *nums表示把nums这个list的所有元素作为可变参数传进去。