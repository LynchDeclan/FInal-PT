import time
import sys

inventory = []
def add_item(item):
    inventory.append(item)
    print(f"You have picked up {item}.")

def main_branch():
    time.sleep(2)
    print("You awaken, feeling dizzy, in what appears to be a small room with wooden walls. After a few moments, you begin to feel a sharp, throbbing pain in your head...")
    time.sleep(2)
    print("A small oil lamp in the corner illuminates the room, and you see that you have been tied to a chair positioned in the center of the room...")
    time.sleep(2)
    print("You hear people arguing angrily on the other side of the rice paper doors to your right, and a small tanto blade on the shelf to your left... ")
    time.sleep(2)
    first_attempt = input("Do you attempt to escape using the blade? Or do you wait for the people outside to enter? (blade/wait)\n")
    first(first_attempt)

def first(first_attempt):
    if first_attempt == "blade":
        time.sleep(2)
        print("You proceed to shuffle, slowly and quietly, in your chair, over to the the blade, and grab it with what little reach you have from behind.")
        add_item("Tanto")
        print("(A Tanto has been added to your inventory)")
        time.sleep(2)
        print("After hiding the blade, you begin to hear the voices outside approaching more closely, until one of the mysteriosu figures opens the paper door...")
        time.sleep(2)
        print("Three, slim, masekd men step through the threshold into the room and face you...")
        time.sleep(1)
        print("You feel the urge to question them on their whereabouts, but the one directly in front of you proceeds to speak:")
        time.sleep(1)
        print("'Helpless soldier of war, there is nothing that needs to be explained, other than the matter of your execution...'")
        time.sleep(2)
        print("You say: 'I was captured? How is this so? I don't remember ever being caught...'")
        time.sleep(2)
        print("They say: 'You have dishonoured your family and your emperor, it is death by seppuku.'")
        time.sleep(2)
        print("You are angered by this statement, you never believed this would be a way to die. For what? You saved the others, but your actions came at the cost of your honour?")
        time.sleep(3)
        break_out = input("If you choose to use the Tanto to break out, say (break).\n If you choose to wait and see what happens next, say (stay).")
        if break_out == "break":
            time.sleep(2)

        if break_out == "stay":
            time.sleep(2)

    if first_attempt == "wait":
        door_list = ["room 1", "room 2", "room 3", "room 4", "room 5", "room 6", "room 7", "room 8",]
        time.sleep(2)
        print("After a few moments, three, slim, masekd men step through the threshold into the room and face you...")
        time.sleep(1)
        print("You feel the urge to question them on their whereabouts, but the one directly in front of you proceeds to speak:")
        time.sleep(1)
        print("'Helpless soldier of war, there is nothing that needs to be explained, other than the matter of your execution...'")
        time.sleep(2)
        print("You say: 'I was captured? How is this so? I don't remember ever being caught...'")
        time.sleep(2)
        print("They say: 'You have dishonoured your family and your emperor, it is death by seppuku.'")
        time.sleep(2)
        print("You are angered by this statement, you never believed this would be a way to die. For what? You saved the others, but your actions came at the cost of your honour?")
        time.sleep(3)
        print("The masked man speaks again: 'You know that there is only one way to regain your honour...' He gestures towards the Tanto on the shelf.")
        time.sleep(2)
        get_out = input("You know that what binds you to the chair feels quite weak, do you attempt to force your way out? (yes/no)\n")
        if get_out == "yes":
            time.sleep(2)
            print("After a brief silence, in front of the eyes of the masked men, you suddenly twist your body to forcefully break out of the binds.")
            time.sleep(1)
            print("Your attempt is successful, and your binds are broken. In a flash, you take all the masked men off their feet and exit the room into a large corridor.")
            time.sleep(2)
            print("You see a large door at the end of the corridor, but the corridor is also lined with smaller doors...")
            time.sleep(2)
            choose_door = input("Do you attempt to run to the door at the end? Or do you choose to go through one of the many doors lining the walls? Hurry, the masked men will attemp to pursue you. (main door/wall door)\n")
            doors(door_list, choose_door)
            

        if get_out == "no":
            time.sleep(2)


def doors(door_list, choose_door):       
    if choose_door == "main door":
        time.sleep(2)
        print("You bolt down the centre of the corridor, with hopes of finding freedom beyond the large door in front of your eyes.")
        time.sleep(2)
        print("For a moment, you take a glimpse behind you and see that it is already too late...")
        time.sleep(2)
        print("You ran out of time. The masked men all grab hold of you and tackle you to the ground.")
        time.sleep(2)
        print("One of them proceeds to open one of the doors lining the walls and throws you into the dark room, where you painfully tumble down what feels like stairs.")
        time.sleep(2)
        print("After stopping at the bottom, you lif youself off the ground to find youself face-to-face with a gigantic serpent.")
        time.sleep(3)
        print("It is in this moment which you suddenly regret your descision of not taking the blade earlier...")
        time.sleep(2)
        sys.exit()

    if choose_door == "wall door":
        time.sleep(2)
        for door in door_list:
            time.sleep(1)
            print(door)
        time.sleep(2)
        choose_door = input("Which door do you choose to go through?:\n")
        door_choices(choose_door)

def door_choices(choose_door):
    if choose_door == "room 1":
        time.sleep(2)
        print("You open the door quickly and then slam it shut behind you, but you were too hasty, the bar on the outside falls and locks you inside...")
        time.sleep(2)
        print("You can hear angry voices, probably the masked men, outside as they start looking through each door...")
        time.sleep(2)
        print("You decide its time to get moving, so you turn around to find a dark tunnel lit by lamps.")
        time.sleep(2)
        print("You definitely do not remember this place. They took you somewhere far, far away.")
        time.sleep(2)
        print("As you start walking, you step on something that appears to be a key...")
        time.sleep(2)
        print("As soon as you lay a finger on it, visions start to overload your mind. A loud voice in you head rings, telling you to collect all the stormwalker keys...")
        time.sleep(1)
        add_item("Stormwalker Key")
        print("(A Stormwalker Key has been added to your inventory)")
        time.sleep(2)
        print("You proceed though the tunnel, you don't understand why, but you feel that these keys are the only way to escape. Where they have put you is no ordinary place...")
        time.sleep(2)
        print("Suddenly, the ground begins collapsing beneath your feat, and you fall into a rocky pit, where you see other dead bodies, samurai.")
        time.sleep(2)
        print("There is a light ahead of you. An exit, perhaps, but blocked by a gigantic stone beast that locks its gaze onto you.")
        sword_or_run = input("Do you choose to take a sword from one of the dead samurai? Or do you choose to run through the danger ahead? (sword/run)\n")
        if sword_or_run == "sword":
            time.sleep(2)
            print("")




        





if __name__ == "__main__":
    main_branch()