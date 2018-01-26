#转义序列

'''

"I am 6'2\" tall."  #将字符串中的双引号转义
'I am 6\'2" tall.'  #将字符串中的单引号转义

'''

tabby_cat = "\tI'm tabbed in."  #\t 一个Tab键的位置
persian_cat = "I'm split\non a line."  #\n 换行
backslash_cat = "I'm \\ a \\ cat."  #\\ 转义反斜杠
test_123 = "this is a test."
my_name = "Bobby"

#三个双引号自动换行，\t一个Tab位
fat_cat = """
I'll do a list:
\t* Cat fodd
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(r"\t\r") #用r定义原始字符串
print(R"\t\n") #用R定义原始字符串

print("这是测试:", test_123)
print("这是测试:", test_123)

print("我的名字是：%r" % my_name) #使用%r传参时，会用引号将所传内容引起来
print("我的名字是：%s" % my_name) #使用%s传参时，不会用引号引起来
print("my name is:",my_name) #第三种传参，所传参数只能放在末尾。
