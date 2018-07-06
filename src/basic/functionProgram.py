import functools
from functools import reduce

# Functional Programming 函数式编程 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。


# Higher-order function
print(abs)
# 此处abs是函数本身，abs(-10)是函数调用
# 函数本身也可以赋值给变量，即：变量可以指向函数。
f = abs
print(f(-10))


# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
# 函数作为参数传递的，就叫高阶函数，higher-order function
def add(x, y, f):
    return f(x) + f(y)


print(add(5, -1, abs))


# 编写高阶函数，就是让函数的参数能够接收别的函数


# map reduce
# map支持传入一个函数和一个iterable，map会将函数作用在列表的每个元素，并作为新的iterable返回, map也是个高阶函数
def power(x):
    return x * x


r = map(power, range(10))
print(list(r))
print(list(map(str, range(10))))


def add(x, y):
    return x + y


print(reduce(add, range(5)))


# reduce将计算结果依次和下一个序列的值做函数运算
def concat(x, y):
    return x * 10 + y


print(reduce(concat, range(6)))

# 完成一个str to int的函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


print(str2int('55321'))


# 用lambda优化，将fn转为lambda
def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def normalize(name):
    return str.upper(name[:1]) + str.lower(name[1:])


# print(list(normalize(['adam', 'LISA', 'barT'])))
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 排序
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))


# 函数作为返回值
def calc_sum(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


# 如果想延迟求和，需要的时候再计算呢，可以不返回结果，返回求和的函数


# 内部函数sum可以引用外部函数lazy_sum的参数和局部变量
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力
def lazy_sum(*args):
    def sum():
        sums = 0
        for x in args:
            sums = sums + x
        return sums

    return sum


print(lazy_sum(range(5)))
f = lazy_sum(1, 3, 5, 7, 9)
print(f())


# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


# <class 'list'>: [<function count.<locals>.f at 0x00000215E26D5D90>, <function count.<locals>.f at 0x00000215E26D5B70>, <function count.<locals>.f at 0x00000215E26D5BF8>]
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


# 函数也是一个对象，函数对象有个熟悉__name__,可以拿到函数的名字
def now():
    print('2018')


print(now.__name__)


# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2018')


# 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
print(now())
print(now.__name__)  # 如果不加@functools.wraps(func)，now已经指向wrapper

# Partial function 偏函数
# 偏函数也可以设定参数的默认值
print(int('12345', base=8))


# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去
def int2(s, base=2):
    return int(s, base)


print(int2('1000000'))

#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2
int2=functools.partial(int,base=2)
#简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
