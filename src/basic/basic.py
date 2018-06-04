# list ['a','b'] 可变集合
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
# tuple tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
# t = (1) 有歧义，python定义这种就是赋值，如果要表示tuple，写成t=(1,)
# if
age = input('age: ')
age = int(age)
if age > 18:
    print('your age is',age)
    print('adult')
else:
    print('teenager')

# for x in 循环

# dict 其他语言的map
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。 要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
print(s)


