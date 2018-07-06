class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


dog = Dog()
dog.run()


# 继承的另一个好处：多态。

def run_twice(animal):
    animal.run()
    animal.run()

# 新增一个Animal的子类，不必对run_twice()做任何修改，实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态

# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思


#动态语言的“鸭子类型”
#java中，如果要传入Animal类型，则传入的对象必须是Animal的子类，而对于python这样的动态语言，只要对象有run方法，就可以认为他是Animal的子类，看上去像个鸭子，就可以看成是个鸭子
class Timer(object):
    def run(self):
        print('Start...')



#总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
# 获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
print(dir(Timer))
print(dir('ABC'))



#由于Python是动态语言，根据类创建的实例可以任意绑定属性。
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90


#千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性
