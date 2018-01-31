print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')  #练习转义字符

#三组双引号括起来的内容会自动换行
poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("----------")
print(poem)
print("----------")


five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)

def secret_formula(started):  #定义函数
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates  #函数具有返回值


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars,crates))

start_point = start_point / 10

#另外一种方式实现一样的效果，即在传参数的时候直接引用函数
print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))
