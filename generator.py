# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# generator保存的是算法

# 第一种方法
# 只要把一个列表生成式的[]改成()，就创建了一个generator
L = [x*x for x in range(1,11)]
print(L)
g = (x*x for x in range(1,11))

# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
# 可以通过next()函数获得generator的下一个返回值
print(next(g))
# 这种不断调用next(g)实在是太变态了，正确的方法是使用for循环

for n in g:
	print(n)

# 斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易
def fib(max):
	n,a,b = 0,0,1
	while n<max:
		print(b)
		a,b=b,a+b
		n=n+1
	return 'done'
# fib函数实际上是定义了斐波拉契数列的推算规则
# 要把fib函数变成generator，只需要把print(b)改为yield b就可以了
def fib(max):
	n,a,b = 0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n=n+1
	return 'done'
	# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator

	# generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
	# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

# 举个简单的例子，定义一个generator，依次返回数字1，3，5
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

# 调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：
# o = odd()
# next(o)