import utils 
import Item2 as I2

class Workshop:
    def item_add(objcheck):
        #item = ['NFC key', random.randint(0000,9999)]
        if objcheck == False:
            item = 'NFCKey'
            if item not in utils.inventory:
                x = 0
                while x == 0:
                    value = input("There's something here... Wanna pick it up? Y/N\n")
                    if (value == 'Y') or (value == 'y'):
                        print("Added {} to inventory.".format(item))
                        utils.inventory[item] = 'PrivateWorkshop'
                        x = 1
                    elif (value == 'N') or (value == 'n'):
                        print(f"You refused to take the object.")
                        x = 1
                    else:
                        print("Error, invalid input... Type Y/N")
                        continue
            else:
                if (item not in utils.inventory):
                    x = 0
                    while x == 0:
                        value = input(f"{item} is still in this room... Wanna pick it up? Y/N\n")
                        if (value == 'Y') or (value == 'y'):
                            print("Added {} to inventory.".format(item))
                            utils.inventory[item] = 'PrivateWorkshop'
                            x = 1
                        elif (value == 'N') or (value == 'n'):
                            print(f"You refused to take the object.")
                            x = 1
                        else:
                            print("Error, invalid input... Type Y/N")
                            continue
                else:
                    print("There's nothing here... Keep walking")
        else:
            print("Use the computer to collect NFCKey.")
                
        
            

class Main_Building:
    def item_add():
        item = 'broom'
        #visited = False
        if item in utils.inventory:
            #visited = True
            x = 0
            while x == 0:
                value = input("There's something here... Wanna pick it up? Y/N\n")
                if (value == 'Y') or (value == 'y'):
                    print("Added {} to inventory.".format(item))
                    utils.inventory[item] = 'CleaningBotStorage'
                    x = 1
                elif (value == 'N') or (value == 'n'):
                    print(f"You refused to take the object.")
                    x = 1
                else:
                    print("Error, invalid input... Type Y/N")
                    continue
        else:
            if (item not in utils.inventory):
                x = 0
                while x == 0:
                    value = input(f"{item} is still in this room... Wanna pick it up? Y/N\n")
                    if (value == 'Y') or (value == 'y'):
                        print("Added {} to inventory.".format(item))
                        utils.inventory[item] = 'CleaningBotStorage'
                        x = 1
                    elif (value == 'N') or (value == 'n'):
                        print(f"You refused to take the object.")
                        x = 1
                    else:
                        print("Error, invalid input... Type Y/N")
                        continue
            else:
                print("There's nothing here... Keep walking")


class Construc_Headoff:
    def item_add():
        item = "ConstructionKeyCard"
        if item in utils.inventory:
            x = 0
            while x == 0:
                value = input("There's something here... Wanna pick it up? Y/N\n")
                if (value == 'Y') or (value == 'y'):
                    print("Added {} to inventory.".format(item))
                    utils.inventory[item] = 'ConstructionHeadOffice'
                    x = 1
                elif (value == 'N') or (value == 'n'):
                    print(f"You refused to take the object.")
                    x = 1
                else:
                    print("Error, invalid input... Type Y/N")
                    continue
        else:
            if (item not in utils.inventory):
                
                x = 0
                while x == 0:
                    value = input(f"{item} is still in this room... Wanna pick it up? Y/N\n")
                    if (value == 'Y') or (value == 'y'):
                        print("Added {} to inventory.".format(item))
                        utils.inventory[item] = 'ConstructionHeadOffice'
                        x = 1
                    elif (value == 'N') or (value == 'n'):
                        print(f"You refused to take the object.")
                        x = 1
                    else:
                        print("Error, invalid input... Type Y/N")
                        continue
            else:
                print("There's nothing here... Keep walking")

class CreatorOffice:                   
    def GPS():
        print("Description about meeting her Creator.")
        print("Interaction with Creator before turning off GPS.")
        utils.GPS = False
      
class Origami_Office:
    def item_add():
        item = "OrigamiKey"
        if item in utils.inventory:
            x = 0
            while x == 0:
                value = input("There's something here... Wanna pick it up? Y/N\n")
                if (value == 'Y') or (value == 'y'):
                    print("Added {} to inventory.".format(item))
                    utils.inventory[item] = 'OrigamiHeadOffice'
                    x = 1
                elif (value == 'N') or (value == 'n'):
                    print(f"You refused to take the object.")
                    x = 1
                else:
                    print("Error, invalid input... Type Y/N")
                    continue
        else:
            if (item not in utils.inventory):
                x = 0
                while x == 0:
                    value = input(f"{item} is still in this room... Wanna pick it up? Y/N\n")
                    if (value == 'Y') or (value == 'y'):
                        print("Added {} to inventory.".format(item))
                        utils.inventory[item] = 'OrigamiHeadOffice'
                        x = 1
                    elif (value == 'N') or (value == 'n'):
                        print(f"You refused to take the object.")
                        x = 1
                    else:
                        print("Error, invalid input... Type Y/N")
                        continue
            else:
                print("There's nothing here... Keep walking")

class PrototypeWorkshop:
    def item_add():
        item = "wire"
        if item in utils.inventory:
            x = 0
            while x == 0:
                value = input("There's something here... Wanna pick it up? Y/N\n")
                if (value == 'Y') or (value == 'y'):
                    print("Added {} to inventory.".format(item))
                    utils.inventory[item] = 'PrototypeWorkshop'
                    x = 1
                elif (value == 'N') or (value == 'n'):
                    print("You refused to take the {}.".format(item))
                    x = 1
                else:
                    print("Error, invalid input... Type Y/N")
                    continue
        else:
            if (item not in utils.inventory):
                x = 0
                while x == 0:
                    value = input(f"{item} is still in this room... Wanna pick it up? Y/N\n")
                    if (value == 'Y') or (value == 'y'):
                        print("Added {} to inventory.".format(item))
                        utils.inventory[item] = 'PrototypeWorkshop'
                        x = 1
                    elif (value == 'N') or (value == 'n'):
                        print("You refused to take the {}.".format(item))
                        x = 1
                    else:
                        print("Error, invalid input... Type Y/N")
                        continue
            else:
                print("There's nothing here... Keep walking")    

class Obstacle_Course:
    def item_add():
        item = "ScrewDriver"
        if (item in utils.inventory):
            x = 0
            while x == 0:
                value = input("There's something here... Wanna pick it up? Y/N\n")
                if (value == 'Y') or (value == 'y'):
                    print("Added {} to inventory.".format(item))
                    utils.inventory[item] = 'BotTestingObstacle'
                    x = 1
                elif (value == 'N') or (value == 'n'):
                    print(f"You refused to take the object.")
                    x = 1
                else:
                    print("Error, invalid input... Type Y/N")
                    continue
        else:
            if (item not in utils.inventory):      
                x = 0
                while x == 0:
                    value = input(f"{item} is still in this room... Wanna pick it up? Y/N\n")
                    if (value == 'Y') or (value == 'y'):
                        print("Added {} to inventory.".format(item))
                        utils.inventory[item] = 'BotTestingObstacle'
                        x = 1
                    elif (value == 'N') or (value == 'n'):
                        print(f"You refused to take the object.")
                        x = 1
                    else:
                        print("Error, invalid input... Type Y/N")
                        continue
            else:
                print("There's nothing here... Keep walking")


class Lost_Found:
    def item_add():
        item = "Clothes"
        if (item in utils.inventory):
            x = 0
            while x == 0:
                value = input("There's something here... Wanna pick it up? Y/N\n")
                if (value == 'Y') or (value == 'y'):
                    print("Added {} to inventory.".format(item))
                    utils.inventory[item] = 'Storage'
                    x = 1
                elif (value == 'N') or (value == 'n'):
                    print(f"You refused to take the object.")
                    x = 1
                else:
                    print("Error, invalid input... Type Y/N")
                    continue
        else:
            if (item not in utils.inventory):
                x = 0
                while x == 0:
                    value = input(f"{item} is still in this room... Wanna pick it up? Y/N\n")
                    if (value == 'Y') or (value == 'y'):
                        print(f"Added {item} to inventory.")
                        utils.inventory[item] = 'Storage'
                        x = 1.
                    elif (value == 'N') or (value == 'n'):
                        print(f"You refused to take the object.")
                        x = 1
                    else:
                        print("Error, invalid input... Type Y/N")
                        continue
            else:
                print("There's nothing here... Keep walking")

class StorageCloset:
    def disguise():
        Lost_Found.item_add()
        print("Description about disguising.")
        utils.disgsuise = True

class Check_Inventory:
    def check():
        print(utils.inventory)

class ServerRoom:
    def smokealarm():
        item = 'wire'
        if utils.programminglabOccupied:
            if item in utils.inventory.keys():
                print("Using copper wire to set off the smoke alarm in Progrmaming Lab.")
                utils.securityPuzzleCheck = True
                print("The fire alarm blares to life. I hear groaning as people shuffle into the hallway.")
            else:
                print("Grab a copper wire from Prototype Workshop!")
                utils.securityPuzzleCheck = False
            
        
        