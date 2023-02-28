import os
# 读文件
f = open('D:/Desktop/demo.txt', 'r')

print(f.read())
f.close()

with open('D:/Desktop/demo.txt', 'r') as f:
    print(f.read())

with open('D:/Desktop/demo.txt', 'w') as f:
    f.write('Hello, world!')

print(os.name)

# 查看当前目录的绝对路径:
os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
os.rmdir('/Users/michael/testdir')