import time


# Setup
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
name = input("Welcome to the jungle explorer we've got fun and games now let's get this party started and tell me your name?\n")
time.sleep(1)
print("Welcome to the unknown, " + name + ".")
time.sleep(2)
print("You awaken in the middle of a forest with a mythical creature fast approaching you!")

# Start of game
response = ""
while response not in yes_no:
    response = input("Shall we get moving?\nyes/no\n")
    if response == "yes":
        print("You are a brave soul "+ name +" \n")
    elif response == "no":
        print("You are the creatures dinner now. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")

# Next part of game
response = ""
while response not in directions:
    print("To your left, you see a large open area with an axe to collect on the way.")
    time.sleep(2)
    print("To your right, there is a large vine wall with an axe resting at the top.")
    time.sleep(2)
    print("Behind, is a narrow passage between two trees that leads to a drop with an axe.")
    time.sleep(2)
    print("Forward leads to the creature.\n")
    time.sleep(2)
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "forward":
        print("The creature eats you. Farewell, " + name + ".")
        quit()
    elif response == "right":
        print("You climb the vine wall, collecting an axe on the way but instantly hit a land slide.\n")
    elif response == "left":
        print("You collect an axe but the floor instantly collapses.\n")
        quit()
    elif response == "backward":
        print("You collect an axe on the way but instantly hit a land slide.\n")
        quit()
    else:
        print("I didn't understand that.\n")


