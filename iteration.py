# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
# 在Python中，迭代是通过for ... in来完成的
# Python的for循环抽象程度要高于Java的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
# list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print("迭代出key值",key)
	#默认情况下，dict迭代的是key。

# 如果要迭代value，可以用for value in d.values()
for value in d.values():
	print("迭代出value值",value)

# 如果要同时迭代key和value，可以用for k,v in d.items()
for k,v in d.items():
	print("迭代出key和value值",k,v)