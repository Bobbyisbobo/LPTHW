ten_things = "Apples Oranges Crows Telephone Light Suger"
print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(" ") #以空格为分隔符对字符串进行切片
print(stuff)
a = input() #input作为程序暂停对开关
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #pop函数用于移除列表中的一个元素，默认移除最后一个元素，并且返回该元素的值。
    print("Adding:", next_one)
    stuff.append(next_one) #append方法用于在列表末尾添加新的对象
    print("There is %d items now." % len(stuff))

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff)) #join函数用于将序列中的元素以指定的字符串链接生成一个新的字符串，本处使用空格链接
print(stuff)
print('#'.join(stuff[3:5])) #对stuff这个字符串的第4和第5个位置的内容以#相连
    
