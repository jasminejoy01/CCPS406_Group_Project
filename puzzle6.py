"""
schedule
"""

import time
headstat = []

#call function when interacting with room computer
# in programming lab or just call it when entering room
def setSchedule():
    x=0
    while x == 0:
        value = input("Welcome!\nWhose schedule would you like to access?\n1. The Creator\n2. Head of Construction\n3. Head of Origami\n0. Exit\n")
        if value == '1':
            print("Admin Access Required")
            time.sleep(1)
        elif value == '2':
            print("Admin Access Required")
            time.sleep(1)
        elif value == '3':
            print("...")
            time.sleep(1)
            print("Access to schedule #3 granted")
            time.sleep(1)
            print("Current schedule: Work\nUpcoming schedule: Meditation ")
            y=0
            while y == 0:
                v = input("Switch to meditation? Y/N")
                time.sleep(1)
                print("Remember to change it now")
                if (v == 'Y') or (v=='y'):
                    print("You hear the Origami Head grumbling and stomping out of their office...\nI think it's safe to go in there now")
                    headstat.append('1')
                    y = 1
                    x = 1
                elif (v == 'N') or (v == 'n'):
                    print("I need to change it")
                else:
                    print("Cmon... That's not even an option")
        elif value == '0':
            x = 1
            print("You've exited the scheduler")
        else:
            print("Error; invalid input")


#from puzzle6 import headstat

#Call when player position == origami head office position
def origamiheadchecker():
    if '1' not in headstat:
        print("The Head seems to still be in the office\nSeems they'll only leave when the schedule is set to Meditation")
        print("I gotta change their schedule... Maybe I can do that at the programming lab?")
        #Place player back to room prior to this one
        #lock em out
    elif '1' in headstat:
        print("You got a key!")
        inventory.append('this key')
        #Add key to inventory function to maeve's inventory

#tester ignore
def main():
    origamiheadchecker()
    setSchedule()
    origamiheadchecker()