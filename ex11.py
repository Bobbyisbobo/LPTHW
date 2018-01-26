#python3 已经不再使用raw_input()了
#python2 中的raw_input()将所有的输入作为字符串看待，返回的字符串类型，而对于input()，它希望能够读取一个合法的python表达式，即你输入的字符串的时候必须使用引号将它括起来，否则它会引发一个SyntaxError。

print("How old are you?")
age = input()
print("How tall are you?")
height = input()
print("How much do you weigh?")
weight = input()

print("So, you're %r old, %r tall and %r heavy." % (age,height,weight))
