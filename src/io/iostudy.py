#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from io import StringIO
import os
import pickle
import json
#Python引入了with语句来自动帮我们调用close()方法
with open('test1.txt', 'r',encoding='utf-8') as f:
    print(f.read())

with open('test1.txt','a',encoding='utf-8') as f:
    f.write('append\n')

#StringIO顾名思义就是在内存中读写str。
str=StringIO()
str.write('hello')
str.write(' ')
str.write('world!')
print(str.getvalue())


#操作目录，文件
print(os.path.abspath('.'))
#新建目录
# os.path.join('/Users/michael', 'test1dir')，os.mkdir('/Users/michael/test1dir')

#shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充
print([x for x in os.listdir('../')])



#序列化
d=dict(name='zy',age=15,score=99)
print(pickle.dumps(d))
with open('test.txt','wb') as f:
    pickle.dump(d,f)

with open('test.txt','rb') as f:
    print(pickle.load(f))



#json
print(json.dumps(d))
