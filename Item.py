import utils
import time

class Item:
    def __init__(self, name, canTake, inInventory, description, interactable, useText):
        self.name = name
        self.canTake = canTake
        self.inInventory = False
        self.description = description
        self.interactable = True
        self.useText = useText

    def take(self, filename):
        if self.canTake:
            self.inInventory = True
            utils.inventory[self.name] = filename
            print("I picked up the {}.".format(self.name))
        else:
            print("I can't do that.")

    def drop(self):
        if self.name in utils.inventory.keys():
            self.inInventory = False
            utils.inventory.pop(self.name)
            print("I remove the {} from my inventory.".format(self.name))
        else:
            print("I can't do that.")
            
    def examine(self):
        print(self.description)

    def use(self):
        if self.interactable:
            print(self.useText)
        else:
            print("I can't do anything with this")

class Computer:
    def __init__(self, name, canTake, inInventory, description, interactable, useText):
      # islocked, description
      self.name = name
      self.islocked = True
      self.canTake = False
      self.inInventory = False
      self.description = description
      self.interactable = True
      self.useText = useText

    def take(self, filename):
        if self.canTake:
            self.inInventory = True
            utils.inventory[self.name] = filename
            print("I picked up the {}.".format(self.name))
        else:
            print("I can't do that.")
            
    def use(self):
      if self.islocked == True:
        tryingPassword = True
        password = input("Please enter the password: \n")
        while (self.islocked) and tryingPassword:
            if password.lower() == "cw19928":
                self.islocked = False
                print("Welcome")
                self.home()
            elif password == "exit":
                tryingPassword = False
                print("I leave the computer")
            else: 
                password = input("Incorrect password. Please try again. Type 'exit' to leave the computer. \n")

    def examine(self):
        print(self.description)

    def home(self):
        print("\nThe screen is covered in files, some of which are 'Ada', 'To do', and 'Spare Key'")
        file = (input("Which should I open?\n")).lower()
        filesplit = file.split()
        if filesplit[0] == "chmod":
            print("Ha, tricky! But no - not allowed")
            self.home()
        elif "ada" in file:
            print("ACCESS DENIED: It took me forever to get her working! I know I'll be tempted to make changes (and probably break her) so SHE'S LOCKED!")
            self.home()
      
        elif "to do" in file or "todo" in file:
            print("The to-do list opens. \n1. Check on AI project [reminder missed] \n2. Hide fun projects in office before Rin comes in from HQ and takes them again... I miss you, Rosie! [reminder snoozed] \n3. Find more things to put on to-do list [reminder missed]\n \nI close it and return to the home screen.")
            self.home()
        elif "spare key" in file:
            print("Downloading spare key to nearest wireless device....")
            time.sleep(1)
            utils.PlayerKeys.append(1)
            
            print("Downloaded!")
            print("I have {}'s key!'".format(self.name))
            print("I'm done with the computer, so I log off.")
        elif "exit" in file:
            print("I log off the computer.")
        else:
           print("That's not a valid command")
           self.home()

class Terminal:
  def __init__(self, key):
    self.name = "terminal"
    self.key = key;
    self.locked = True;

  def use(self):
    if len(utils.PlayerKeys) == 0:
      print("It seems to require an NFC key that I don't have yet.")
    else:
      if self.key in utils.PlayerKeys:
          print("I scanned my key and the door clicked open.")
          self.locked = False
      else:
        print("It look's like I'll need a key from this deparment's head to unlock it.")


  def examine(self):
    print("The terminal reads \n\'LOCKED\'")

class Computer2:
  #Computer in programming lab
  def __init__(self):
    self.name = "computer"

  def use(self):
    if not utils.programminglabOccupied:
        #computer.getSchedule()
        utils.origamiHeadChecker = False
    else:
        print("There are no computers available in this lab. You'll need to get someone to leave...")