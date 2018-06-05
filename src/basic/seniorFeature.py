from collections import Iterable
import os
# 切片 slice  从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2,类似于java里的subString
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[:3])
print(L[-2:])
print('ABCDEFG'[::2])


def trim(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        return s
    elif s[:1] == ' ':
        return trim(s[1:])
    else:
        return trim(s[:-1])


print(trim('  hello   '))


#循环 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for key,value in d.items():
    print(key,' ',value)

#判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
print(isinstance('abc', Iterable)) # str是否可迭代)

for i, value in enumerate(['A', 'B', 'C']):
    print(i,value)


#列表生成式 list comprehensions
# 运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁
print([x*x for x in range(1,11)])
print([m+n for m in 'ABC' for n in 'XYZ'])
print([d for d in os.listdir()])



# generator,生成器，节省空间，实时推算下一个值
g=(x * x for x in range(10))
print(isinstance(g,Iterable))

#一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

g=fib(6)
while True:
    try:
        print(next(g))
    except StopIteration as e:
        print('Generate return value:',e.value)
        break

