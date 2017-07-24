# 定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回。
# 自定义一个求绝对值的my_abs函数

def my_abs(x):
	if x > 0:
		return x
	else:
		return - x

print(my_abs(0))
print(my_abs(-1))

# 定义空函数
# 占位符作用
def nop():
	pass


# 数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x



# 返回多个值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny