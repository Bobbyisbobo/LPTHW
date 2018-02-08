#!/usr/local/bin/python3
#—*— coding: utf-8 _*_
#猜数字游戏，数字区间为0～100

from sys import exit
import getpass

def Guess_Number(number):
    a = number
    x = 0
    y = 100

    while True:
        b = int(input("请输入一个0～100以内的数字："))

        #猜测的数字不在区间[x， y]以内时
        if b < x or b > y:
            print("请输入一个[%d， %d]的整数。" % (x, y))

        #猜测的数字大于被猜测的数字，且小于区间上限
        elif b > a and b <= y:
            b -= 1
            y = b
            print("新区间为[%d, %d]" % (x, y))

        #猜测的数字小于被猜测的数字，且大于区间下限
        elif b < a and b >= x:
            b += 1
            x = b
            print("新区间为[%d, %d]" % (x, y))

        #猜中时
        elif b ==a:
            print("恭喜你踩雷了。答案就是%d" % a)
            exit(0)  #正常退出整个程序，exit(1)为异常退出整个程序

        #以防其他异常情况
        else:
            print("这是一个异常退出，囧！")
            exit(1)  #异常的退出

while True:
    guess_number = getpass.getpass("请输入一个数字让大家猜：")

    #确认输入的是数字，且在规定的区间内
    if guess_number.isdigit() == True and 0 <= int(guess_number) <= 100:
        guess = Guess_Number(int(guess_number))
        break #退出本while循环
    
    else:
        print("你输入的数字不是0～100以内的整数。")
    


