def die(why):
    print(why, "there is something wrong.")

a = int(input("Please input a number:"))

if a > 10:
    print("a is bigger than 10.")
else:
    die("not bigger than 10")

