def add(a, b): #定义一个加法函数
    print("Adding %d + %d" % (a, b))
    return(a + b)

def substract(a, b):  #定义一个减法函数
    print("Substracting %d - %d" % (a, b))
    return(a - b)

def multiply(a, b):  #定义一个乘法函数
    print("Multiplying %d * %d" % (a, b))
    return(a * b)

def divide(a, b):  #定义一个除法函数
    print("Diciding %d / %d" % (a, b))
    return(a / b)

print("Let's do some math with just functions!")

age = add(30, 5) #调用加法函数
height = substract(74, 4)  
weight = multiply(90, 2)
iq = divide(300, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

#A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
