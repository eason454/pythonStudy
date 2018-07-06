import logging
logging.basicConfig(level=logging.INFO)
#发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因
try:
    print('try...')
    r=10/0
    print(r)
except ZeroDivisionError as e:
    print('except',e)
finally:
    print('finally')
print('end')


#常见的错误类型和继承关系看这里：
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
#如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2
# Python内置的logging模块可以非常容易地记录错误信息：
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('end')



#断言 assert n != 0, 'n is zero!'
#启动Python解释器时可以用-O参数来关闭assert

