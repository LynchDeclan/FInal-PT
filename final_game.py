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
    time.slee(2)
    print("You hear people arguing angrily on the other side of the rice paper doors to your right, and a small tanto blade on the shelf to your left... ")
    time.sleep(2)
    first_attempt = input("Do you attempt to escape using the blade? Or do you wait for the people outside to enter? (blade/wait)\n")
    first(first_attempt)

def first(first_attempt):
    if first_attempt == "blade":
        time.sleep(1)

    if first_attempt == "wait":
        time.sleep(1)


if __name__ == "__main__":
    main_branch()