# Functional Programming 函数式编程 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。


#Higher-order function
print(abs)
#此处abs是函数本身，abs(-10)是函数调用
#函数本身也可以赋值给变量，即：变量可以指向函数。
f=abs
print(f(-10))
