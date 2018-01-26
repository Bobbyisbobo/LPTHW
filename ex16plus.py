from sys import argv

script, filename = argv

target = open(filename,'r') #以只读的形式打开文件
print(target.read())  #一定要打印出来，才会显示

target.close()
