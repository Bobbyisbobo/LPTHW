a = 10
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

print("I said: %r." % x)
print("I also said: '%s'." % y) #y中已经存在don't带单引号，所以想再用单引号就只能用'%s'来传参
print("I also said: %r." % y)  #y中已经存在don't带单引号，为了便于区分就会把单引号自动变为双引号

print("I also said: %r." % binary) #用%r来传参时，如果所传参数是字符串则会自动加上引号，所传参数中已经自带单引号，则会用双引号，否则，用单引号
print("I also said: %s." % binary)

print("I also said: %r" % a)  #用%r来传参时，如果所传参数是数字则不会添加引号
print("I also said: %s" % a)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "This is the left side of ..."
e = "a string with a right side."

print(w+e)
