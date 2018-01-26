from sys import argv #从sys模块中导入argv

script, filename = argv  #将argv解包，每个参数赋予一个变量名

txt = open(filename)  #用open()命令打开文件

print("Here's your file %r:" % filename)  #显示文件名
print(txt.read())  #用txt的read命令来读取文件内容并打印出来

txt.close() #文件打开后一定要关闭，这点很重要
'''
print("Type the filename again:")
file_again = input(">")  #写死的文件名变成从外部获取的方式

txt_again = open(file_again)  #用open命令打开文件

print(txt_again.read()) #读取文件并打印出来

txt_again.close()  #文件打开后要关闭，这点很重要
'''
