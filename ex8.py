formatter = "%r %r %r %r"

print(formatter % (1,2,3,4)) #传参数
print(formatter % ('one','two','three','four'))  #传参数
print(formatter % (True, False, False, True)) #传参数
print(formatter % (formatter,formatter,formatter,formatter))  #formatter被视为字符串
print(formatter % (
    'I had this thing.',
    'That you could type up right.',
    "But it didn't sing",
    "So I said goodnight."
    ))
