# 定义函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x


print(my_abs(-99))


# my_abs('A')

# 空函数，定义还没想好怎么写的函数
def nop():
    pass


# 返回多个值 其实返回的是一个值，是tuple，在语法上，返回一个tuple可以省略括号
# 函数的默认参数 ，默认参数要牢记一点：默认参数必须指向不变对象！
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Adam', 'M', city='Tianjin')


# 默认参数的坑
def add_end(L=[]):
    L.append('END')
    return L


print(add_end())
print(add_end())


# 修复一下
def add_end(l=None):
    if l is None:
        l = []
    l.append('END')
    return l


# 可变参数  参数numbers接收到的是一个tuple
def calc(*number):
    sum1 = 0
    for x in number:
        sum1 = sum1 + x * x
    return sum1


print(calc(2, 3))

# 如果已有一个tuple，这么调 ,*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见
nums = [1, 2, 3]
calc(*nums)


# 关键字参数,使用**,这些关键字参数在函数内部自动组装为一个dict
# 可以扩展函数功能，例如正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')


# name: Michael age: 30 other: {}
# name: Bob age: 35 other: {'city': 'Beijing'}


# 命名关键字参数  函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查
# 例如想限制只能传入指定的某2个key
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def namedKeyParamPerson(name, age, *, city, job):
    print(name, age, city, job)

# 必须传入参数名，否则报错 改例子中，person只有2个位置参数positional arguments，如果不传参数名，python认为你传了4个
person('Jack', 24, city='Beijing', job='Engineer')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：以下例子因为有了*args这个可变参数，所以后面就不在需要单独的*来表示
# 命名关键字参数了,命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值
def person(name, age, *args, city, job):
    print(name, age, args, city, job)



def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass




#参数组合 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)



def product(*x):
    if not x:
        raise TypeError('x should be not empty')
    sum1=1
    for i in x:
       sum1=sum1*i
    return sum1
# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
