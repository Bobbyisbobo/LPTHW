print("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')  #传参时，如果时直接传的字符串时，需要用引号引起来
print("And everywhere that Mary went.")
print("$" * 10)  #what'd that do? 重复双引号内的内容10次

end1 = 'C'
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

# watch that comma at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6,) #，放在末尾没有影响
print(end7 + end8 + end9 + end10 + end11 + end12,)
