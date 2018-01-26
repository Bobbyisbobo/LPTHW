#自定义一个函数并使用4中传参数的方式

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of Crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the functioni numbers directly:")
# 直接调用函数，并直接传入参数
cheese_and_crackers(20,30)


print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
# 将需要传入的参数传给自变量，然后调用函数时通过自变量来传入参数
cheese_and_crackers(amount_of_cheese, amount_of_crackers)



print("We can even do math inside too:")
# 参数也可以通过运算传入
cheese_and_crackers(10 + 20, 4 + 5)


print("And we can combine the two, variables and math:")
#传入参数的方式可以综合自变量和运算
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)
