#import time

headstat=[]
prototype_flag = []

#inventory = [] #remove this

#Trigger puzzle by trying to visit the 'Obstacle Course' room
def puzzle4():
    visited = False
    if visited == False:
        if 'Construction Bot' in inventory:
            visited = True
            print("You controlled the Construction Bot to move the blockage")
        elif 'Key 3' in inventory:
            visited = True
            print("You used the Head of Construction's Card to use nearby machinery to move the blockage")
        else:
            print("I'm not strong enough to move this blockage...\nThere's some machines and we've got some construction bots that can move these things with")
            #Set player position back into previous position
    else:
        print("Location: Bot Testing Room")

#Trigger when entering construction office
def constructionchecker():
    if '2' in headstat:
        print("Location: Construction Head Office")
    elif '1' not in headstat:
        print("You can't do much here... The Head is in there\nHe loves his creations\nTry breaking one of his prototypes")
        prototype_flag.append('1')#triggers breakbot
        #Place player back to previous location
    elif '1' in headstat:
        inventory.append('Key 3')
        headstat.append('2') #triggers first clause next visit
        print("You've acquired the Construction Head's Key")

#Triggers when player position == construction bot position
def consbot():
    if 'Key 3' in inventory: #change to checking maeve's inventory
        inventory.append('Construction Bot') #append to proper inventory
        print("Construction Bot Acquired")
    else:
        print("This door needs the construction head's key to open")


def breakbot():
    print("You start breaking every prototype you see")
    print("As you leave the room, you see a panicked Construction Head leave his office\nNow's your chance!")
    headstat.append('1')

#TRIGGER THIS NOT BREAKBOT when visiting the prototype workshop!!!!!!!!!!
def breakbotcheck():
    if '1' in prototype_flag:
        breakbot()
    else:
        print("Current Location: Prototype Workshop")
'''
puzzle4()
time.sleep(1)
breakbotcheck()
time.sleep(1)
consbot()
time.sleep(1)
constructionchecker()
time.sleep(1)
breakbotcheck()
time.sleep(1)
constructionchecker()
time.sleep(1)
constructionchecker()
time.sleep(1)
puzzle4()'''