import time

character_name = ''


answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]


sword = 0

required = ("\nUse only A, B, C, D\n")

character_name = input('please enter the name of your character: ')

print("\nWELCOME TO THE ADVENTURE GAME ð®\n")
print(f"{character_name} wakes up in a dark and foggy forest. There is a certain peace in the forest.ð²\nYou want to get up but you feel pain in your left leg.")


def intro():

    print("You look around and notice that the path behind you is closed by a rocky mountain.â°\nIn the far right there is a little light whose source is not known.\nThe path on the left is also impassable by a lot of felled trees.\nYou look ahead and find nothing but darkness.")
    time.sleep(1)
    print(
        "Which path will you choose???\n\nA: forward â¬\nB: right â¡\nC: bakcwards â¬\nD: left â¬")
    choice = input(">>> ")
    if choice in answer_A:
        option_dark_path()
    elif choice in answer_B:
        option_light()
    elif choice in answer_C:
        print("How do you want to climb a mountain with this injured foot???ð\n")
        intro()
    elif choice in answer_D:
        print("I do not think it is possible to pass through all these felled treesð©\n")
        intro()
    else:
        print(required)


def option_dark_path():
    print("\nYou gather all your strength and slowly walk towards the darkness.\nYou try not to feel the pain in your left leg and you feel that little by little your eyes got used to the darkness.ð\nSuddenly you hear a sound from behind the trees and your heart beat rises rapidly.ð¨")
    time.sleep(1)
    print("What would you do???\n\nA: Go back â¬\nB: move deeper in the darkness")
    choice = input(">>> ")
    if choice in answer_A:
        intro()
    elif choice in answer_B:
        option_move_deeper()
    else:
        print(required)


def option_move_deeper():
    print("\nYou walk deeper into the forest and you hear a sound from behind the trees.ðð»\nYou try not to pay attention to the sound and move forward.\nSuddenly you see a creature hovering in the air next to a tree staring at you with its red eyes.ð§ð»ââï¸")
    time.sleep(1)
    print("\nWhat would you do???\n\nA: Go Back â¬\nB: Find a rock and throw at it ð§±\nC: Move towards it and try pass it â¬\n")
    choice = input(">>> ")
    if choice in answer_A:
        intro()
    elif choice in answer_B:
        print("The creature is angry and come closer and bites your neck!!!ð´")
        print("YOU ARE DEAD!!!\nâââ!!!GAME OVER!!!âââ")
    elif choice in answer_C:
        if sword == 0:
            print(
                "The creature block your path and wants to fight you.\nYou do not have a weapon and The creature bites your neck!!!ð´")
            print("YOU ARE DEAD!!!\nâââ!!!GAME OVER!!!âââ")
        else:
            print(
                "You fight with all your being and use the âswordâ to overcome the creature and move on untill you see the city light.")
            print("ððCongratulations you've done it ðð")
    else:
        print(required)


def option_light():
    print("\nAs you approach the light, you see that the dim light was the refletion of moonlight on a metal object.\nYou bend down and try to pick up the object and realize that the object is a samurai sword.\nYou look around and realize that there is no way forward and you have to go back to where you were before. ð¡ð¡ð¡")
    time.sleep(1)
    print("What would you do???\n\nA: Go Back â¬\nB: Wait for no reason\n")
    global sword
    sword = 1
    choice = input(">>> ")
    if choice in answer_A:
        intro()
    elif choice in answer_B:
        print("Use your head and go backð§ ")
        option_light()
    else:
        print(required)


intro()
