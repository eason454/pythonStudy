# 一个.py文件就称之为一个模块（Module）
# 模块还可以避免函数名和变量名冲突
# python所有内置函数 https://docs.python.org/3/library/functions.html
#每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包



#作用域
#正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc


#第三方库 https://pypi.org/
