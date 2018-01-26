###方式一：从sys导入argv
from sys import argv  #从sys中导入argv

script, filename = argv  #将argv解包,将argv视为一个元组
##

###方式二：用input的方法
#filename = input()
##

'''
方式一和方式二的区别：方式一在直接运行这个脚本的时候就直接将需要的参数传入，不需要先执行这个脚本后，再重新一步步传入参数。
'''

print("We are going to erase %r." % filename)  #询问是否清空该文件
print("If you don't want that, hit CONTROL-C(^C).")  #control+c系统自动强行退出脚本
print("If you do want that, hit RETURN.")  #回车继续脚本

input("?")  #这步输入基本没有什么用，可以视为暂停脚本的执行


print("Opening the file..")
target = open(filename,'w')  #以写入的形式打开文件，“W”如果没有该文件则会自动创建一个新的文件

print("Truncating the file. Goodbye!")
target.truncate()  #清空该文件，注意这个操作需要慎用

print("Now I'm going to ask you for three lines.")

###方式一：写入操作分两步，第一步先将需要写入的参数赋予一个变量，然后再根据变量一个一个传入参数
'''
line1 = input("Line1:")  #将传入的参数赋予一个变量
line2 = input("Line2:")
line3 = input("Line3:")

print("Im going to write these to the file.")

target.write(line1)  #写入文本
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''
###方式二：传入一个参数，就立即写入到文本中
target.write(input("line1:")) #通过参数写入到文本中
target.write(input("line2:"))
target.write(input("line3:"))

print("And finally, we close it.")
target.close()  #打开文档后一定要关闭该文档，这个习惯要养成

