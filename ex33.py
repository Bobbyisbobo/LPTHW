'''
from sys import argv
script, number, plus = argv

i = 0
numbers = []
while i < int(number):
    print("At the top i is %d" % i)
    numbers.append(i)
    i += int(plus)
    print("Numbers now:", numbers)
    print("At the bottom i is %d" % i)

print("The numbers: ")
for num in numbers:
    print(num)
'''

'''
def numbers_append(number, plus):
    i = 0
    numbers = []
    while i < int(number):
        print("At the top i is %d" % i)
        numbers.append(i)
        i += int(plus)
        print("Now numers:", numbers)


numbers_append(10, 2)
'''

i = 0
numbers = []

for i in range(0, 6):
    print("At the top i is %d" % i)
    numbers.append(i)
    i += 1
    print("Now numbers:", numbers)
    print("At the bottom i is %d" % i)
