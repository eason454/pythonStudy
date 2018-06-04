# 定义函数
def my_abs(x):
    if not isinstance(x,(int,float)):
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
