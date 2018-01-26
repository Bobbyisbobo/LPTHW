# -- coding: utf-8 --

name = "Bobby"
my_age = 30 #a lie
my_height = 68 #inches (a lie)
my_weight = 150 #lbs
my_eyes = "Black"
my_teeth = "White"
my_hair = "Brown"

print("Let's talk about %s." % name) #传参时，所传值为字符串时用%s表示
print("He's %d inches tall." % my_height) #传参时，所传值为数字时用%d表示
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes,my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# This line is tricky, try to get it exactly right

print("If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight))

#用format的形式来传递参数
print("This is {number} {fruit}.".format(fruit="apple", number="an"))
