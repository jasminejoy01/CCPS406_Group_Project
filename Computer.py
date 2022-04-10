#The PC in the Private Workshop

import time
import utils

class Computer:
    def __init__(self):
      self.name = "computer"
      self.canTake = False
      self.inInventory = False
      self.description = "A fairly modern PC. Some sticky notes line the edges of the monitor. A keyboard sits in front of it on the desk."
      self.interactable = True
      self.useText = ""
            
    def use(self):
        tryingPassword = True
        password = input("Please enter the password: \n")
        while tryingPassword:
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