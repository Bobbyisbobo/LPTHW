'''
from sys import argv
script, filename = argv
'''
print("This is a review, you should know all the things you have learnt before.")

def this_is_what_have_learnt(filename):
    study = open(filename)
    print(study.read())
    study.close()
    
filename = input()
text = this_is_what_have_learnt(filename) #在调用函数前一定要定义函数
