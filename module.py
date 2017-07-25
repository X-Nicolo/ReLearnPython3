# 为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里
# 这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式
# 在Python中，一个.py文件就称之为一个模块（Module）

# 使用模块有什么好处？

# 最大的好处是大大提高了代码的可维护性。
# 其次，编写代码不必从零开始。当一个模块编写完毕，就可以被其他地方引用。
# 我们在编写程序的时候，也经常引用其他模块，包括Python内置的模块和来自第三方的模块。
# 引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。
# 现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。
# 每一个包目录下面都会有一个__init__.py的文件
# 这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。
# __init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。

# 使用模块


# 以内建的sys模块为例，编写一个hello的模块：

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
__author__ = 'Nicolo'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

# 第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；

# 第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

# 第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

# 以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。

# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
# 运行python3 hello.py获得的sys.argv就是['hello.py']；
# 运行python3 hello.py Nicolo获得的sys.argv就是['hello.py', 'Nicolo']。

# 注意到这两行代码：

# if __name__=='__main__':
#     test()

# 在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__
# 而如果在其他地方导入该hello模块时，if判断将失败
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。


# 安装第三方模块

pip install XXX