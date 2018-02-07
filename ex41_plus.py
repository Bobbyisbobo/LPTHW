from sys import exit
from random import randint

class Game(object):

    def __init__(self, start):
        self.quips = [
            "You died. You kinda suck at this.",
            "Your mom would be proud. If she were smarter.",
            "Such a loser.",
            "I have a small puppy that's better at this."
        ]
        self.start = start


    def play(self):
        next = self.start

        while True:
            print("*" * 50)
            room = getattr(self, next)
            next = room()


    def death(self):
        print(self.quips[randint(0, len(self.quips) - 1)])
        exit(1)

    def central_corridor(self):
        print("The Gothons of Planet Percal #25 have invaded your ship and destroyed")

        action = input(">")

        if action == "shoot":
            print("Quick on the draw you yank out your blaster and fire it at the Gothon.")
            return "death"

        elif action == "dodge":
            print("Like a world class boxer you dodge, slip and slide right")
            return "death"

        elif action == "tell a joke":
            print("Lucky for you they made you learn Gothon insults in the academy.")
            return "laser_weapon_armory"
        
        else:
            print("DOES NOT COMPUTE!")
            return "central_corridor"

    def laser_weapon_armory(self):
        print("You do a dive roll into the Weapon Armory, crouch and scan the room")
        code = "%d%d%d " % (randint(1, 9), randint(1, 9), randint(1, 9))
        guess = input(">")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]>")

        if guess == code:
            print("The container clicks open and the seal breaks, letting gas out.")
            return "the_bridge"
        else:
            print("The lock buzzes one last time and then you hear a sicking")
            return "death"

    def the_bridge(self):
        print("You burst onto the Bridge with the netron destruct bomb")

        action = input("> ")

        if action == "throw the bomb":
            print("In a panic you throw the bomb at the group of Gothons")
            return "death"

        elif action == "slowly place the bomb":
            print("You point your balster at the bomb under your arm")
            return "escape_pod"
        else:
            print("DOES NOT COMPUTE!")
            return "the_brige"

    def eacape_pod(self):
        print("You rush through the ship desperately trying to make it to")

        good_pod = randint(1, 5)
        guess = input("[pod #] >")

        if int(guess) != good_pod:
            print("You jump into pod %s and hit the eject button." % guess)
            return "death"
        else:
            print("You jump into pod %s and hit the eject button." % guess)
            exit(0)

a_game = Game("central_corridor")
a_game.play()
            
            

        
        
