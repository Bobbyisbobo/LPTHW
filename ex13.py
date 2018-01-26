#这个练习需要用命令行来启动

from sys import argv
'''
first = input("fisrt:")
second = input("second:")
third = input("third:")
'''
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
