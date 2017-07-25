# 函数式编程
# 高阶函数
# 变量可以指向函数
f = abs
print(f(-10))
# 变量f现在已经指向了abs函数本身。直接调用abs()函数和调用变量f()完全相同。


# 传入函数
def add(x,y,f):
	return f(x) + f(y)

print(add(-1,-2,abs))



