
import sys;

# hello world 

print('hello world for Jarron')



# print hellowrld with variable 
def hello(name, id):
    print('hello world in function')
    print('name is :', name)
    print('id is :', id)


def showpythonversion():
    print('python version is :', sys.version)

# call hello function
hello(name = '林杰為', id = 1100507)

showpythonversion()