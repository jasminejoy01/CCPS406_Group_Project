import utils

class Item:
    def __init__(self, name, canTake, inInventory, description, interactable, useText):
        self.name = name
        self.canTake = True
        self.inInventory = False
        self.description = description
        self.interactable = True
        self.useText = useText

    def take(self):
        if self.canTake:
            self.inInventory = True
            utils.inventory.append(self.name)
            print("I picked up the {}.".format(self.name))
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
      self.canTake = True
      self.inInventory = False
      self.description = description
      self.interactable = True
      self.useText = useText

    def take(self):
        if self.canTake:
            self.inInventory = True
            utils.inventory.append(self.name)
            print("I picked up the {}.".format(self.name))
        else:
            print("I can't do that.")
            
    def use(self):
      if self.islocked == True:
        tryingPassword = True
        password = input("Please enter the password: \n")
        while (self.islocked) and tryingPassword:
            if password == "cw19928":
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
        print("The screen is covered in files, some of which are 'Ada', 'To do', and 'Spare Key'")
        file = (input("Which will you open?\n")).lower()
        filesplit = file.split()
        if filesplit[0] == "chmod":
            print("Ha, tricky! But no - not allowed")
            self.home()
        elif "ada" in file:
            print("ACCESS DENIED: It took me forever to get her working! I know I'll be tempted to make changes (and probably break her) so SHE'S LOCKED!")
            self.home()
      
        elif "to do" in file or "todo" in file:
            print("1. Check on AI project [reminder missed] \n2. Hide fun projects in office before Rin comes in from HQ and takes them again... I miss you, Rosie! [reminder snoozed] \n3. Find more things to put on to-do list [reminder missed]")
            self.home()
        elif "spare key" in file:
            print("Downloading spare key to nearest wireless device....")
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
    for i in range(len(utils.PlayerKeys)):
      if utils.PlayerKeys[i] == self.key:
        self.locked = False;
        print("I touched the terminal and it scanned my NFC key. The door clicked open.")
      else: print("It seems to require an NFC key that I don't have yet.")
    if len(utils.PlayerKeys) == 0:
      print("It seems to require an NFC key that I don't have yet.")

  def examine(self):
    print("The terminal reads \n\'LOCKED\'")
