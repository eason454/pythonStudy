class Student(object):#表示该类是从哪个类继承下来的
    #构造方法，self表示创建的实例本身
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('name:%s,score:%s' % (self.name,self.score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()


def print_score(std):
    print('%s,%s' % (std.name,std.score))
print_score(bart)



#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
