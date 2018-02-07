from sys import exit
import getpass

def Guess_Number(number):
    a = number
    x = 0
    y = 100

    while True:
        b = int(input("请输入一个0～100以内的数字："))
        
        if b < 0 or b > 100:
            print("请输入一个[0， 100]的整数。")

        elif b > a and b < y:
            y = b
            print("新区间为[%d, %d]" % (x, y))

        elif b < a and b > x:
            x = b
            print("新区间为[%d, %d]" % (x, y))

        elif b < x or b > y:
            print("输入有误。请输入一个[%d, %d]的数字。" %(x, y))
            
        else:
            print("棒棒哒！你猜中了。正确答案就是%d" % a)
            exit(0)
            
number = int(getpass.getpass("请输入需要猜测的数字："))
guess = Guess_Number(number)
