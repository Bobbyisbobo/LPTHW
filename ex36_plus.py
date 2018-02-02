import random

def die(script):
    print(script, "game over buddy!")

print("Life is full of advantures, which door will you open: 1, 2, 3, 4")
door_number = int(input("Enter a door number:"))
door_chose = random.randint(1, 6)
print("Opus, I said life is full of advanture, you will enter room %d, now let's go!" % door_chose)

def tiger_room(number):
    print("""You are entering room 1.
Be careful, there is a tiger over there.
Now, what will you do:
\t1.Close the door.
\t2.Enter the room.
\t3.Crying.
""")
    room_chose = int(input("chose a number: 1, 2 or 3"))
    if room_chose == 1:
        print("You can chose anthoer room:1, 2, 3, 4")
        door_chose == int(input())
        if door_chose == 1:
            tiger_room(1)
        elif door_chose == 2:
            lion_room(2)
        elif door_chose == 3:
            wolf_room(3)
        elif door_chose == 4:
            gold_room(4)
        else:
            die("Bad luck!")
    else:
        die("Bad luck!")
   
def lion_room(number):
    print("""You are entering room 2.
Be careful, there is a lion over there.
Now, what will you do:
\t1.Close the door.
\t2.Enter the room.
\t3.Crying.
""")
    room_chose = int(input("chose a number: 1, 2 or 3"))
    if room_chose == 1:
        print("You can chose anthoer room:1, 2, 3, 4")
        door_chose == int(input())
        if door_chose == 1:
            tiger_room(1)
        elif door_chose == 2:
            lion_room(2)
        elif door_chose == 3:
            wolf_room(3)
        elif door_chose == 4:
            gold_room(4)
        else:
            die("Bad luck!")
    else:
        die("Bad luck!")
    

def wolf_room(number):
    print("""You are entering room 3.
Be careful, there is a wolf over there.
Now, what will you do:
\t1.Close the door.
\t2.Enter the room.
\t3.Crying.
""")
    room_chose = int(input("chose a number: 1, 2 or 3"))
    if room_chose == 1:
        print("You can chose anthoer room:1, 2, 3, 4")
        door_chose == int(input())
        if door_chose == 1:
            tiger_room(1)
        elif door_chose == 2:
            lion_room(2)
        elif door_chose == 3:
            wolf_room(3)
        elif door_chose == 4:
            gold_room(4)
        else:
            die("Bad luck!")
    else:
        die("Bad luck!")

def gold_room(number):
    print("""You are entering room 4.
Oh, my god, you are entering the gold room.
Now, what will you do:
\t1.Take 10 unit gold.
\t2.Take 1000 unit gold.
\t3.Take as much as you can.
""")
    room_chose = int(input("chose a number: 1, 2 or 3"))
    if room_chose == 1:
        print("You can chose anthoer room:1, 2, 3, 4")
        door_chose == int(input())
        if door_chose == 1:
            tiger_room(1)
        elif door_chose == 2:
            lion_room(2)
        elif door_chose == 3:
            wolf_room(3)
        elif door_chose == 4:
            gold_room(4)
        else:
            die("Bad luck!")
    else:
        die("Bad luck!")
    

if door_chose == 1:
    tiger_room(1)
elif door_chose == 2:
    lion_room(2)
elif door_chose == 3:
    wolf_room(3)
elif door_chose == 4:
    gold_room(4)
else:
    die("Bad luck!")
    
    

