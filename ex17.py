'''
思路：
1.运行一个拷贝文档的脚本，在运行的时候就传入拷贝源文件名和需要拷入的文件名，所以用到sys中的argv
2.需要判断拷贝源和拷入的文件是否存在，所以用到os.path中的exists
3.打开拷贝源文件open()，并且读取需要拷贝到内容read()
4.打开需要拷入到文件open(),将从拷贝源拷贝出来的内容写入到需要拷入的文件中
5.最后一定要关闭打开的文件
'''

from sys import argv  #从sys中导入argv
from os.path import exists  #从 os.path 中导入 exists，exists的作用是用来判断文件是否存在

script, from_file, to_file = argv #将argv解包

print("Copying from %s to %s" % (from_file, to_file))

#we could do these two on one line too,how?

input_data = open(from_file)  #打开拷贝源
indata = input_data.read()  #从拷贝源中读取到拷贝到数据并将其传给变量indata


print("The input file is %d bytes long" % len(indata)) #len()统计indata内容的字符长度

print("Does the input file exist? %r" % exists(from_file))
print("Does the output file exist? %r" % exists(to_file)) # exists()命令：将文件名字符串作为参数，如果文件存在的话，它将返回True，否则将返回False。用以判断需要拷入的文件是否存在。
print("Ready, hit Return to continue, Control-C to abort.")
input()  #这个没有实际作用，可以理解为暂停作用，让用户选择退出脚本或者继续脚本。

output = open(to_file, 'w') #以写入的形式打开需要拷入的文件
output.write(indata)  #将从拷贝源读取的内容写入到需要拷入的文件中

print("Aright, all done.")

output.close()  #关闭打开的文件
input_data.close()  #关闭打开的文件

