'''
from sys import argv

script, arg1, arg2 = argv
'''

def my_first_function_test(arg1, arg2):
    print("this is the first arg: % d." % arg1)
    print("this is the second arg: % d." % arg2)

# 直接传入参数
my_first_function_test(10, 20)

#通过变量传参数
a = 10
b = 30
my_first_function_test(a, b)

#通过运算传入参数

my_first_function_test(10 + 10, 20 + 2)
