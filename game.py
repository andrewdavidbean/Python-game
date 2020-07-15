# import time

# def level_two():
#     time.sleep(1)
#     response2 = input("I'm so glad you said yes, lets learn shall we? [Okay/Nah]")
#     if response2 == "Okay" or response2 == "okay" or response2 == "Ok" or response2 == "ok" or response2 == "OK":
#         print("Okay, first things first...")
#         time.sleep(3)
#     print("I could carry on.. But this is all for now, but please study what you've just read :)")
# ​
# def level_one():
#     time.sleep(1)
#     response1 = input("Are you ready?... [Yes/No]")
#     if response1 == "Yes" or response1 == "yes" or response1 == "Y" or response1 == "y":
#         print("Areeeee Youuuuu Sureeeeeeeeeee??? :)")
#         level_two()
#     elif response1 == "No" or response1 == "no" or response1 == "N" or response1 == "n":
#         print("Fine. Be that way and learn on your own terms!")
# ​
# def start_game():
#     response = input("Hey there, how are you today? [Good/Bad]")
#     if response == "Good" or response == "good":
#         print("Amazing, I'm great too!.. Thanks for asking...")
#     elif response == "Bad" or response == "bad":
#         print("Wow.. Somebodies a grumpy bum..")
#     else:
#         print("I'm sorry, I didn't quite catch that, let me ask again..")
#         start_game()
#     time.sleep(1)
#     print("...Anyway, I almost forgot to ask..")
#     global name
#     name = input("What is your name? ")
#     time.sleep(1)
#     print("Why hello there {}, it's so great to meet you, My name is Jay.".format(name))
#     time.sleep(1)
#     response = input("Do you want to learn something cool with code!? [Y/N] ")
#     if response == "Y" or response == "y" or response == "Yes" or response == "yes":
#         print("Great! Check this out! :).")
#         level_one()
#     elif response == "N" or response == "n" or response == "No" or response == "no":
#         print("Fine then, be that way. Goodbye.")
#     else:
#         print("Try again, I didn't recognise that.")
#         start_game()
# start_game()

# # Setup
# yes_no = ["yes", "no"]
# directions = ["left", "right", "forward", "backward"]
 
# # Introduction
# name = input("What is your name, adventurer?\n")
# print("Greetings, " + name + ". Let us go on a quest!")
# print("You find yourself on the edge of a dark forest.")
# print("Can you find your way through?\n")
 
# # Start of game
# response = ""
# while response not in yes_no:
#     response = input("Would you like to step into the forest?\nyes/no\n")
#     if response == "yes":
#         print("You head into the forest. You hear crows cawwing in the distance.\n")
#     elif response == "no":
#         print("You are not ready for this quest. Goodbye, " + name + ".")
#         quit()
#     else: 
#         print("I didn't understand that.\n")
 
# Next part of game
response = ""
while response not in directions:
    print("To your left, you see a bear.")
    print("To your right, there is more forest.")
    print("There is a rock wall directly in front of you.")
    print("Behind you is the forest exit.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print("The bear eats you. Farewell, " + name + ".")
        quit()
    elif response == "right":
        print("You head deeper into the forest.\n")
    elif response == "forward":
        print("You cannot scale the wall.\n")
        response = "" 
    elif response == "backward":
        print("You leave the forest. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")



# print("You find a chest! Looks like something interesting could be inside!")
# response = raw_input("Open the chest? [Yes/No]")
# if response == "Yes" or response == "yes":
#         print("*You open the chest and find the following items...")
#         print("")        
# treasure_chest1 = ["diamonds", "gold", "silver", "sword"]
# for treasure in treasure_chest1:
#         print(treasure)
# print("")
# print("Take all {} treasures, press '1'".format(len(treasure_chest1)))
# response = raw_input("")
# if response == "1":
#         print("You have removed {} items from the chest".format(len(treasure_chest1)))
#         print("")
