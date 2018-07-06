from types import MethodType
from enum import Enum, unique


# 动态语言的灵活性，可以创建了对象后，给对象随时绑定任何属性‘
class Student(object):
    pass


s = Student()
s.name = 'zhao yi'
print(s.name)


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)
print(s.age)


# 使用__slot__限制实例的属性，比如，只允许对Student实例添加name和age属性

class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()
s.name = 'eason'
# s.score=50
s.age = 12


# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的


# property， 为了校验set的属性值，可以写一个方法提供给外部调用，但是不直观，我们可以直接@property来把一个方法转成属性调用
class Student():
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value


s = Student()
s.score = 30
print(s.score)


# s.score = 150


# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。


# 多重继承，一个子类就可以同时获得多个父类的所有功能   设计通常称之为MixIn
class Mammal():
    pass


class RunnableMixIn():
    pass


class CarnivorousMixIn():
    pass


class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass


# Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name


print(Student('zhao'))


# __iter__,__getitem__,__get_attr

# __call__
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('zhao ')
s()

# 判断一个对象是否能被调用
print(callable(Student('zhao')))
print(callable(max))

# 枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday(1))
print(Weekday.Fri)


# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)


# Hello是一个class，它的类型就是type
print(type(Hello))
h = Hello()
# h是一个实例，它的类型就是class Hello
print(type(h))


# 创建class的方法就是使用type()函数

# 动态创建一个类
def fn(self,s='world1'):
    print("hello %s" % s)


Hello1=type('Hello2', (object,), dict(hello=fn))
h=Hello1()
h.hello()


# 先定义metaclass，就可以创建类，最后创建实例
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        print('mappings:',mappings)
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
