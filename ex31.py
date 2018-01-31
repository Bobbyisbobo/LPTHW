print("You enter a dark room with two doors. Do you\
 go through door 1 or door 2?")
door = input(">")

if door == "1":
    print("""
There's a giant bear here eating a cheese cake.\
What do you do?
1. Take the cake.
2. Scream at the bear.
3. Just fighting.
""")
    bear = input(">")

    if bear == "1":
          print("The bear eats your face off. Good job!")
    elif bear == "2":
          print("The bear eats your legs off. Good job!")
    else:
          print("Well, doing %s is probably better. Bear runs away.")
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("""
1. Blueberries.
2. Yellow jacket clothespins.
3. Understanding revolers yelling melodies.
""")

    insanity = input(">")
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job.")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job.")
elif door == "3":
    print("Are you sure, you will fighting with a bear?")
    print("""
1. Yes.
2. No.
3. Crying.
""")

    fighting = input(">")
    
    if fighting == "1":
        print("You win. Good job!")
    elif fighting == "2":
        print("You are just a little children.")
    else:
        print("Don't crying, just run away!")

else:
    print("You stumble around and fall on a knife an die. Game Over.")
        
