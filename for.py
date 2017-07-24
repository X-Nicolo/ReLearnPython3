# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
names = ['Michael', 'Bob', 'Tracy']
for name in names:
	print (name)
	# 所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。

# 计算1-10的整数之和，可以用一个sum变量做累加
sum = 0
for n in [1,2,3,4,5,6,7,8,9,10]:
	sum = sum +n
print(sum)
# 如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数
# 可以生成一个整数序列，再通过list()函数可以转换为list。
# print(list(range(101)))
sum1 = 0
for n in list(range(101)):
	sum1 = sum1 + n
print(sum1)