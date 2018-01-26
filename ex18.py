#函数：迷你脚本
#在自己到脚本中创建自己到命令
# this one is like your scripts with argv
def print_two(*args):  #定义一个函数
    arg1, arg2 = args  #将参数解包
    print("arg1: %r, arg2: %r" % (arg1,arg2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2): #定义一个函数，但是在python中可以跳过整个参数解包到过程
    print("arg1: %r, arg2 %r" % (arg1,arg2))

# this just takes one argument
def print_one(arg1):  #定义一个新函数，只需要传递一个参数
    print("arg1: %r" % arg1)

# this one takes no arguments
def print_one_again():  #也可以定义一个函数，但是不需要传递任何参数
    print("I got nothing.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_one_again()
    
