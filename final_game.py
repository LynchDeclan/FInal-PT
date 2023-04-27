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
        break_out = input("If you choose to use the Tanto to break out, say (break). If you choose to wait and see what happens next, say (stay).\n")
        if break_out == "break":
            time.sleep(2)
            print("Your attempt is successful, and your binds are broken. In a flash, you manage to slit the throat of who appears to be the leader of the masked men and run out of the room into a large corridor.")
            time.sleep(2)
            print("You see a large door at the end of the corridor, but the corridor is also lined with smaller doors...")
            time.sleep(2)
            choose_door = input("Do you attempt to run to the door at the end? Or do you choose to go through one of the many doors lining the walls? Hurry, the masked men will attemp to pursue you. (main door/wall door)\n")
            doors(door_list, choose_door)

        if break_out == "stay":
            time.sleep(2)
            print("The masked man speaks again: 'You know that there is only one way to regain your honour...' He gestures towards the shelf...")
            time.sleep(2)
            print("You reaslise that the Tanto was there for your sepukku ritual...")
            time.sleep(2)
            print("But you still have it in your hands...")
            time.sleep(2)
            print("In a flash, the masked man rips you out of your binds and puts heavy chains on your hands.")
            time.sleep(2)
            print("He says: 'This one needs to be put in special containment.")
            time.sleep(2)
            print("Swiftly, they drag you out of the room into a large corridor, where they throw you into one of the rooms and lock the door behind you.")
            time.sleep(3)
            print("You look around. It is a cell with a high ceiling and a single, square window at the top.")
            time.sleep(2)
            print("It is then when you see an old man sitting with his back turned to you on the only bench in the cell. With a large sword at his side.")
            time.sleep(2)
            print("You still have the Tanto blade concealed in your garnments from earlier, you managed to hide it from the masked men successfully...")
            time.sleep(2)
            kill_or_not = input("Do you find the old man a threat and kill him silently? Or do you call out to him? (kill/call)\n")
            if kill_or_not == "kill":
                time.sleep(2)
                print("In a poised position, you suddenly lunge at the man, in hopes of disarming and killing him.")
                time.sleep(2)
                print("But, almost as suddenly, he and the sword are gone, and you notice the point of a blade sticking out of your chest.")
                time.sleep(2)
                print("You start coughing blood and soon collapse onto the ground.")
                time.sleep(2)
                print("The old man's face is visible, and you suddenly start to hear voices getting louder and louder inside your head.")
                time.sleep(2)
                print("Visions start to overload your mind. A loud voice in your head rings, telling you to collect all the stormwalker keys...")
                time.sleep(2)
                print("The old man places his hand on your wound, raises it, and a mysterious object starts to materialise... A very large, silver key...")
                time.sleep(2)
                print("Your wound then starts to close, and you gan your strength back. You have healed from a fatal injury, but you don't know how...")
                time.sleep(2)
                print("You yell at the old man: 'What- What happened to me!?'")
                time.sleep(2)
                print("He says: 'I am sorry, but you were the opportunity I needed.'")
                time.sleep(2)
                print("You say: 'What do you mean?'")
                time.sleep(2)
                print("He says: 'I finally got a chance to use this sword... What I pulled out of yur body, was a mix of divine energy from the sword and a human heart...'")
                time.sleep(3)
                print("'The only ingredients to create a Stormwalker Key...'")
                time.sleep(2)
                print("You notice him placing the key he holds into the hollow hilt of the sword, making a satisfying click sound...")
                time.sleep(2)
                print("The sword then starts glowing a magnificent blue colour...")
                time.sleep(2)
                print("He says: 'The longer a key stays outside, the more it decays. It no longer glows silver and turns into a different colour. It becomes unable to guide you to his realm...'")
                time.sleep(2)
                print("Whose realm?")
                time.sleep(2)
                print("He says: 'Take the sword, my time is already over, and destroy this wall with it...'")
                time.sleep(2)
                print("You slash the wall with the sword. The mark turns into a bright blue colour, and the wall blasts open...")
                time.sleep(2)
                add_item("Stormwalker Sword")
                print("(A Stormwalker Sword has been added to your inventory)")
                time.sleep(2)
                print("You feel the air from outside, but you are at the top of a mountain, large trees below...")
                time.sleep(2)
                print("You suddenly fall forward in response to a push from the old man: 'Find my master!', he says")
                time.sleep(2)
                print("You dive downinto the trees, and enter a tunnel in the ground, falling faster and faster, you then enter a chasm with glowing silver walls, until you hit the water...")
                time.sleep(2)
                print("But there are no depths, and, as if you have entered a magical portal, you suddenly smash through wooden beams and finally collide with the ground of a stone cave...")



            if kill_or_not == "call":
                time.sleep(2)
                print("You call out to the man who sits in front of you, who looks at you almost as if he is examining you.")
                time.sleep(2)
                print("Suddenly, he appears in front of you, impaling you through the chest with his sword.")
                time.sleep(2)
                print("You start coughing blood and soon collapse onto the ground.")
                time.sleep(2)
                print("The old man's face is visible, and you suddenly start to hear voices getting louder and louder inside your head.")
                time.sleep(2)
                print("Visions start to overload your mind. A loud voice in your head rings, telling you to collect all the stormwalker keys...")
                time.sleep(2)
                print("The old man places his hand on your wound, raises it, and a mysterious object starts to materialise... A very large, silver key...")
                time.sleep(2)
                print("Your wound then starts to close, and you gan your strength back. You have healed from a fatal injury, but you don't know how...")
                time.sleep(2)
                print("You yell at the old man: 'What- What happened to me!?'")
                time.sleep(2)
                print("He says: 'I am sorry, but you were the opportunity I needed.'")
                time.sleep(2)
                print("You say: 'What do you mean?'")
                time.sleep(2)
                print("He says: 'I finally got a chance to use this sword... What I pulled out of yur body, was a mix of divine energy from the sword and a human heart...'")
                time.sleep(3)
                print("'The only ingredients to create a Stormwalker Key...'")
                time.sleep(2)
                print("You notice him placing the key he holds into the hollow hilt of the sword, making a satisfying click sound...")
                time.sleep(2)
                print("The sword then starts glowing a magnificent blue colour...")
                time.sleep(2)
                print("He says: 'The longer a key stays outside, the more it decays. It no longer glows silver and turns into a different colour. It becomes unable to guide you to his realm...'")
                time.sleep(2)
                print("Whose realm?")
                time.sleep(2)
                print("He says: 'Take the sword, my time is already over, and destroy this wall with it...'")
                time.sleep(2)
                print("You slash the wall with the sword. The mark turns into a bright blue colour, and the wall blasts open...")
                time.sleep(2)
                add_item("Stormwalker Sword")
                print("(A Stormwalker Sword has been added to your inventory)")
                time.sleep(2)
                print("You feel the air from outside, but you are at the top of a mountain, large trees below...")
                time.sleep(2)
                print("You suddenly fall forward in response to a push from the old man: 'Find my master!', he says")
                time.sleep(2)
                print("You dive downinto the trees, and enter a tunnel in the ground, falling faster and faster, you then enter a chasm with glowing silver walls, until you hit the water...")
                time.sleep(2)
                print("But there are no depths, and, as if you have entered a magical portal, you suddenly smash through wooden beams and finally collide with the ground of a stone cave...")



    if first_attempt == "wait":
        door_list = ["room 1", "room 2", "room 3", "room 4"]
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
            print("The masked men untie you and proceed to lead you out of the room.")
            time.sleep(2)
            print("The move towards a large door at the end of the corridor.")
            time.sleep(2)
            print("")

def stone_cave():
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
        print("After stopping at the bottom, you lift youself off the ground to find youself face-to-face with a gigantic serpent.")
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
        print("Suddenly, the ground begins collapsing beneath your feat, and you fall into a rocky pit, where you see other dead bodies, samurai...")
        time.sleep(2)
        print("There is a light ahead of you. An exit, perhaps, but blocked by a gigantic stone beast that locks its gaze onto you.")
        time.sleep(2)
        sword_or_run = input("Do you choose to take a sword from one of the dead samurai? Or do you choose to run through the danger ahead? (sword/run)\n")
        if sword_or_run == "sword":
            time.sleep(2)
            print("You take the sword in your hands, it feels almost familiar to the weapon which you once owned, but it feel much heavier, and the design, you notice, is slightly abonormal...")
            time.sleep(1)
            add_item("Stormwalker Katana")
            print("(A Stormwalker Katana has been added to your inventory)")
            time.sleep(2)
            print("You notice that the hilt is hollow, and something falls out, what looks like a silver, ancient key, but unnaturally large...")
            time.sleep(2)
            print("You look up at the beast, staring at you intently, as your body quivers in fear.")
            time.sleep(2)
            print("Then you notice it. One of the beast's red eyes has a darkness in the center, shaped like a large keyhole...")
            time.sleep(2)
            print("You pick up the key and hold it up to the beast...")
            time.sleep(1)
            add_item("Soecial-Grade Stormwalker Key")
            print("(A Special-Grade Stormwalker key has been added to your inventory)")
            time.sleep(2)
            print("Suddenly, the beast growls and abruptly attacks by thrusting its large spear in your direction.")
            time.sleep(2)
            print("You manage to parry the heavy blow by sidestepping and causing the spear to bounce off of your sword and get stuck in the ground")
            time.sleep(2)
            print("You quickly run up the spear and onto the beast's body, heading for its face with this key in your hand.")
            time.sleep(2)
            print("As the beast pulls out the spear and violently reels back, you fly up into the air, but your path stays the same, you thrust the key into the eye of the beast and, wth force, twist it to the right.")
            time.sleep(2)
            print("The beast's upper body starts to crack and collapse. As it hits the ground, it's face splits in two, revealing the inside of it's head...")
            time.sleep(2)
            print("All around the inside, you see different coloured keys with the same design, engraved into the walls of the beast's head...")
            time.sleep(2)
            print("As you collect each of the keys, enormous double-doors start to materialise on the wall behind you...")
            time.sleep(1)
            add_item("Blue Stormwalker Key")
            print("Blue stormwalker key added to your inventory")
            time.sleep(1)
            add_item("Red Stormwalker Key")
            print("Red stormwalker key added to your inventory")
            time.sleep(1)
            add_item("Indigo Stormwalker Key")
            print("Indigo stormwalker key added to your inventory")
            time.sleep(1)
            add_item("Crystalline Stormwalker Key")
            print("Crystalline stormwalker key added to your inventory")
            time.sleep(3)
            print("You notice the four keyholes on the doors, but you also turn and see the small tunnel that leads to light...")
            time.sleep(2)
            which_exit = input("Do you choose to go through the large doors or the small tunnel in hopes of finding an exit? (large doors/small tunnel)\n")
            two_exits(which_exit)
            
        if sword_or_run == "Run":
            time.sleep(2)
            print("You think quickly and attempt to run through the legs of the beast, and towarda the light through the tight tunnel that lies ahead.")
            time.sleep(2)
            print("Suddenly, you hear a thunderous roar from the beast, and you turn around just in time to notice the gigantic spear that it thrusts in your direction, impaling you with it. ")
            time.sleep(2)
            print("You look up with the last ounce of your strength, and notice the glowing red eyes of the beast, staring as you fall off the spear and bleed to death...")
            time.sleep(3)
            sys.exit()
    
    if choose_door == "room 2":
        time.sleep(2)

    if choose_door == "room 3":
        time.sleep(2)
        print("You quickly open the door and run into the room, but you painfully tumble down what feels like stairs that you just discovered. You were too hasty.")
        time.sleep(2)
        print("After stopping at the bottom, you lift youself off the ground to find youself face-to-face with a gigantic serpent.")
        time.sleep(3)
        print("But it is only seconds before you are surrounded by darkness...")
        time.sleep(2) 
        sys.exit()
    
    if choose_door == "room 4":
        time.sleep(2)
        print("You quickly open the door and run into the room, but you painfully tumble down what feels like stairs that you just discovered. You were too hasty.")
        time.sleep(2)
        print("After stopping at the bottom, you lift youself off the ground to find youself face-to-face with a gigantic serpent.")
        time.sleep(3)
        print("But it is only seconds before you are surrounded by darkness...")
        time.sleep(2)
        sys.exit()

def two_exits(which_exit):
    time.sleep(2)




        





if __name__ == "__main__":
    main_branch()