#列表生成器
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
# 生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list(range(1, 11))
print(a)

# 生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
#方法一
l = []
for x in range(1,11):
	l.append(x*x)
print("方法一",l)

# 方法二
L = [x*x for x in range(1,11)]
print("方法二",L)
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
L2 = [x*x for x in range(1,11) if x % 2 ==0]
print("筛选出仅偶数的平方",L2)

# 还可以使用两层循环，可以生成全排列
L3 = [m + n for m in "ABC" for n in "XYZ"]
print("生成全排列",L3)

# 列出当前目录下的所有文件和目录名
# 运用列表生成式，可以写出非常简洁的代码。

import os
L4 = [d for d in os.listdir('.')]
print("列出当前目录下的所有文件和目录名",L4)

# 列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
L5 = [k+'='+ v for k,v in d.items()]
print("使用两个变量来生成list",L5)

# 把一个list中所有的字符串变成小写：
L6 = ['Hello', 'World', 'IBM', 'Apple']
L7 = [s.lower() for s in L6]
print("所有的字符串变成小写",L7)
