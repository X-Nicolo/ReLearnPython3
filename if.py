# 输入用户年龄，根据年龄打印不同的内容，在Python程序中，用if语句实现：
age = 24
if age > 18:
	print("他的年龄是",age)
	print("他长大了")
else:
	print("他还是个小男孩")

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')