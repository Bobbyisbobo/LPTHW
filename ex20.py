from sys import argv  #从sys中导入argv

script, input_file = argv  #解包argv 

#定义一个读取文本的函数，先read(),然后打印出来
def print_all(f):
    print(f.read())

#定义一个函数将文件的指针指向文件的开始
def rewind(f):
    f.seek(0)

#定义一个打印一行文本的函数，需要传入两个参数，第几行和文件名
def print_a_line(line_count, f):
    print(line_count, f.readline())

#打开需要读取的文件
current_file = open(input_file)

print("First let's print the whole file:\n")

#调用第一个print_all()函数
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

#调用第二个函数将文件的指针指向文件的开始
rewind(current_file)

print("let's print three lines:")

current_line = 1
print_a_line(current_line, current_file) #调用打印一行的函数

#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

current_file.close()
