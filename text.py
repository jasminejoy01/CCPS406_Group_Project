# -*- coding: utf-8 -*-
"""
Text
"""

def intro():
    print("I find myself in the dark corner of a room, wires connected to multiple locations on my body. As I wake up, the wires disconnect. I have a User's Guide.")

def readUserGuide():
    print("\nHello! Welcome to the world! I can't believe this actually worked! Well, I hope it worked... But if you're reading this, I must've finally cracked the code on a stable-ish mind! Or rather, my darling Ada must've figured it out and got you all loaded up. She was actually my 8th attempt at an algorithm that uses machine learning to develop a better machine learning algorithm - fitting for my lucky number!\n")
    print("Anyway, you, my beautiful creation, are actually alive! It might take some getting used to, but you'll be able to do all sorts of amazing things. I hope to meet you very soon! I should be by shortly to check on you. Ah, it might be hard to find time, though. You see, I wasn't exaaaactly supposed to be inventing new life... Ugh, Rin's always on me about 'profits' and 'safety' and 'not needing to call the ethics comitee every time I find a new project'. 'No, Cords, you can't just try to invent a whole new branch of science when you haven't even finished the last three projects we let you start!' She just doesn't understand the joy of discovery! That's what science is about! Am I rambling? I'm rambling. Well, see you soon!\n")

def help():
    print("Commands: look, n, north, s, south, e, east, w, west, examine [object], take [object], use [object], read [object], where am i, yes, y, no, n, exit, inventory, gamemap")

def gamemap():
    import csv
    with open('map.txt', 'r') as file:
        reader = csv.reader(file, delimiter = '\t')
        for row in reader:
            print(row)

class PrivateWorkshop:
    def basicDes():
        print ("[Private Workshop] \n I find myself in the dark corner of a room, wires connected to multiple parts of my body. As I boot up, the wires disconnect automatically and the monitor’s bright lights fade away. \n Nearby is a desk with a computer setup and some paper scattered around. \n Next to the desk is a trash bin with some crumpled pieces of paper inside. \n On the West side of the room is a closed door with light shining in from the other side.")
              
    def fancyDes():
        print ("[Private Workshop] \n I'm back in the same dark room where I woke up from. \n I never noticed how dark it is in this room, I'd better turn on the lights. \n After turning the lights on, I notice that the computer is still on, and the small metal trash bin sits beside the desk. The notes inside the bin are different colors; a bright pink and a vibrant orange. \n On the West is [Housekeeping Storage Bay].")

class CleaningBotStorage:
    def basicDes():
        print("[Housekeeping Storage Bay] \n This room is well lit and sparkling clean. There are robots connected to wires which feed into monitors on either side of them. \n There are shelves and storage containers covering a majority of the room; they’re fully stocked with bleach, soap, and other types of cleaning supplies. \n There are brooms neatly stacked on a storage rack near the door to the West. \n Beside the door is another NFC Terminal identical to the one found in the other room.")

    def fancyDes():
        print("[Housekeeping Storage Bay] \n Returning back to this room, I realize how much cleaner it is compared to the rest of the compound; not a speck of dust anywhere. \n There's less items in here than when I had woken up.")

class Greenspace:
    def basicDes():
        print("[Outdoor Break Area] \n I'm surrounded by many employees who are walking to and from different benches, tables, and areas. \n Upon closer inspection, it's clear that this area has a lot more foliage compared to the rest of the pathway; there are significantly more sections of shrubbery and plants, along with rows of large trees providing shade for the people below. \n The path to the East leads to [North Garden Pathway].")
    
    def fancyDes():
        print("[Outdoor Break Area] \n There are still many employees working outdoors. They're all wearing similar uniforms, but I notice now that each employee has their own accessories. Some have different colored/branded lanyards, others have a combination of pins, buttons, earrings, and other jewelry that seem to make each person more unique. \n The abundance of trees and flowers out here are amazing; they all vary in colors, designs, and the trees that offer shade for everyone, also are host to different small animals and fruits. The colors and beauty of the foliage have to be the main attraction of this space. \n The path to the East leads to [North Garden Pathway].")
    
class OutdoorNorth:
    def basicDes():
        print("[North Garden Pathway] \n As I exit the building I see many people walking around, all wearing a similar uniform; the crest on their arms reads: 'NASA'. \n There are tall walls that surround the North of the pathway; cameras are stationed on the edges of the walls, facing inside and outside. Logic states that the tall walls surround the buildings. \n The path to the South streches far; people and other robots can be seen walking in and out of the various buildings. \n The path to the East leads to the door I came from. Above the door reads a sign: 'Housekeeping Storage Bay' \n The path to the West leads to an area filled with benches where people are sitting together in groups. This area looks different compared to the others to the South, but I can't reason why..")
    
    def fancyDes():
        print("[North Garden Pathway] \n There are still many employees walking around the pathway. \n The path stretches south, people and other robots can be seen walking in and out of the various buildings. \n The path to the East leads to [Housekeeping Storage Bay]. \n The path to the West leads to [Outdoor Break Area].")

class OutdoorMiddle:
    def basicDes():
        print("[Middle Garden Pathway] \n I'm at the center of the outdoor pathway. \n The path to the North leads towards the building I had booted up from. \n The path to the South leads to the other end of the pathway; it leads to another building. There is a robot holding a broom, it appears they are using it to move debris off the pathway. \n The path to the West leads to an entrance for a much larger building compared to what you've observed. There's an employee sitting at the desk in-between two gates wearing a different uniform compared to the others. Her uniform has the same insignia as the others, but underneath it reads 'SECURITY'. \n The path to the East leads to a building similar to the one I came from. Above the door reads a sign: Construction Storage Bay'")
    
    def fancyDes():
        print("[Middle Garden Pathway] \n I'm back at the center of the outdoor pathway. \n The path to the North leads to [North Garden Pathway]. \n The path to the South leads to [South Garden Pathway]. \n The path to the West leads to [Main Facility Entrance]; I see the same guard sitting at the desk in-between two gates. \n The path to the East leads to [Construction Storage Bay]. Looking at the building again, I realize that it has a slightly different look compared to [Housekeeping Storage Bay]; this building has a larger door, and also has other large entrances where supplies are being moved through.")

class OutdoorSouth:
    def basicDes():
        print("[South Garden Pathway] \n I'm at the southmost part of the pathway. \n The path to the North leads up to the Middle Garden Pathway. \n The path to the East leads to another building, similar to the previous two, but unique? Above the door reads a sign: 'Abstract Solutions Storage Bay' \n The robot holding the broom is still removing the debris off the pathway. They carry the NASA insignia on their arm, and on their chest reads a number: ''#11'.")

    def fancyDes():
        print("[South Garden Pathway] \n I'm at the southmost part of the pathway. \n The path to the North leads to [Middle Garden Pathway]. \n The path to the East leads to [Abstract Solutions Storage Bay]. \n The robot holding the broom has since finished their task, and has moved on to wiping the windows of the Abstract Solutions Storage Bay. \n Observing this building again, I notice that it has a completely different look compared to the other two storage bays. The walls twist and turn differently, nothing at all like the plain, straight walls that protect the other storage bays.")

class ConstructionBotStorage:
    def basicDes():
        print("[Construction Bot Storage] \n The layout of this building is organized differently than the Housekeeping storage. \n The shelves are in the center of the room, and there are racks lined up against the walls; all of them stocked with different types of construction material. ")
    
    def fancyDes():
        print("[Construction Bot Storage] \n I never noticed how much wooden furniture is used in this building; all the shelves and racks are made up of different types of wood. \n Anything and everything in this room is made up of a beautiful combination of different colored wood. \n What a unique feature.")

class ConstructionHeadOffice:
    def basicDes():
        print("[Construction Head's Office] \n A spacious room with plenty of locked storage cabinets covering the walls of the room. \n There is a lone desk at the far end of the room with a computer and chair. \n Around the room are different types of containers, all holding rolled up sheets of paper. \n One such container is right beside the door; looking at the contents of the paper, it appears to be a design for a 'Moon Habitat'. \n To the West is [Hallway - Section 3]")
    
    def fancyDes():
        print("[Construction Head's Office] \n The Construction Head's Office looks the same as when I had visited earlier. \n Looking around again, there's not much difference compared to when I first came, except it's clear that the Construction Head has a clear love for wooden items. \n His desk is wooden, his shelves are wooden; it appears that everything in here might have been built by them. \n To the West is [Hallway - Section 3]")
        
class OrigamiBotStorage:
    def basicDes():
        print("[Abstract Solutions Storage Bay] \n Despite it's unique exterior, the inside of this storage bay is identical to the one for Housekeeping. \n The shelves line the walls and they're full of different machine parts.")
    
    def fancyDes():
        print("[Abstract Solutions Storage Bay] \n Coming back, I realize how intricate these machine parts are on the shelves; they're all capable of folding in different directions. \n What interesting pieces of technology, I wonder what they can be utilized for.")

class BuildingEntranceExit:
    def basicDes1():
        print("[Main Facility Entrance]\n I'm standing near the Security Checkpoint, there is a security guard at the desk watching the screens in front of her. \n Looking around, I see that there are trails of dirt and debris following the path that the employees take to go in and out of the building.") 

    def basicDes2():
        print("[Main Facility Entrance]\n I'm at the Security Checkpoint. The same security guard is at the desk watching the screens in front of her. \n There are no heavy trails of dirt on the path of the employees, I suspect that she won't bother me about having to clean anything before continuing past.")
      
    def fancyDes():
        print("[Main Facility Entrance]\n I'm back near the Security Checkpoint for the Storage Bays. There's a bored-looking guard sitting behind a desk, idly filling out a sudoku book. She hardly looks up as I pass. The tiled floor still seems reletively clean.")

class ProgrammingLab:
    def basicDes():
        print("[Programming Lab] \n This room is filled with desks and computers as far as my eyes can see. The only other features that this room has are the 'FIRE' lights placed all over the ceiling. \n There are many NASA staff scattered throughout the room, all of them glued to their computer screens. \n To the West is [Hallway - Section 2]")
    
    def fancyDes():
        print("[Programming Lab] \n This room is filled with desks and computers as far as my eyes can see. \n I notice now that the different desks and computers have people's names on them; it also looks like a lot of the desks have been personalized, perhaps by their specific users. \n To the West is [Hallway - Section 2]")

class BotTesting:
    def basicDes():
        print("[Robotics Testing Facility - Basic Functions] \n I find myself in a large and spacious area with tables scattered throughout the room; it appears as if there are multiple workstations with varying activities. A screwdriver sits on one of them. \n To the west is a door with a sign above it, though I can't read it because there is heavy machinery blocking my view. \n There's a robot hooked up to a terminal nearby, much larger than me and the other robots I've seen. \n To the East is [Hallway - Section 1]")
    
    def fancyDes():
        print("[Robotics Testing Facility – Basic Functions] \n I'm back inside the Robotics Testing Facility, the room that has all the types of tests placed on different tables. \n To the West is [Bot Testing - Obstacle Course] \n To the East is [Hallway - Section 1]")
    
class BotTestingObstacleCourse:
    def basicDes():
        print("[Robotics Testing Facility – Obstacle Course] \n The lights in the room turn on after I step through the door; this room looks a lot bigger on the inside than it does on the outside.\n Looking around the room, there are areas that are sectioned off as if there are separate tasks in this room. \n There are beams and platforms organized all around the room, it appears to be a room for testing one's ability to move effectively. \n To the East is [Robotics Testing Facility - Basic Functions]")
    
    def fancyDes():
        print("[Robotics Testing Facility – Obstacle Course] \n The beams and platforms organized all around the room are still here, but there's so much more to this room than I originally noticed. \n The beams and platforms all around the room have different colors marked on them as if to indicate the varying levels of skills; there are paths with a Green line through it, some have Yellow lines, and a rare few have Red colored lines.\n The Red colored paths look like they have the most difficult obstacles to get through. \n To the East is [Robotics Testing Facility - Basic Functions]")

class PrototypeWorkshop:
    def basicDes1():
        print("[Prototype Workshop]\nThis room is very cluttered; there are gears and bits of wire scattered everywhere on the floor, in storage containers, and on the tables.\nThe robots in this room look like they're a mixture of the other models I've seen on the compound.\nOn one of the tables near the door is one of the more complete looking robots, there are papers beside it that read 'Construction 1.6 Prototype'; it looks fairly fragile in this state.\nAcross the room, a burly man seems to be working on something. His jacket is draped over his chair. \nTo the East is the door that leads back into [Hallway - Section 1]")

    def basicDes2():
        print("[Prototype Workshop]\nThis room is very cluttered; there are gears and bits of wire scattered everywhere on the floor, in storage containers, and on the tables.\nThe robots in this room look like they're a mixture of the other models I've seen on the compound.\nThe large man is hunched over the Construction prototype, delicately reassembling it. His jacket is unattended, draped over a chair.\nTo the East is the door that leads back into [Hallway - Section 1]")
  
    def fancyDes1():
        print("[Prototype Workshop]\nThis room is still filled with many colorful spare parts and tools.\nThe bins have a dizzying array of different colored wires, printing material, and spare parts.\nA robot labled 'Construction 1.6 Prototype' lies still on a table. It is made up of mismatched coloured parts. A burly man is carefully working on some new project, wires and circuitry spilling over the table in front of him. His jacket is drapped across his chair. \nTo the East is [Hallway - Section 1]")

    def fancyDes2():
      print("[Prototype Workshop]\nThis room is still filled with many colorful spare parts and tools.\nThe bins have a dizzying array of different colored wires, printing material, and spare parts.\nThe man I now recognize must be Dr.George Ediface carefully cradles his prototype, working with surprising delicacy to reassemble it. His jacket is unattended, draped over a chair.\nTo the East is [Hallway - Section 1]")
    
class PrintingLab:
    def basicDes():
        print("[3D Printing Lab] \n I walk into a very bright room with plenty of desks and chairs all throughout. \n The sun is coming in through the large windows that touch both the ceiling and the floor. \n On each of the tables is a 3D Printer accompanied by clear plastic bins underneath them, containing discarded printing projects. \n At the other end of the room, behind thick walls of glass, sits 3D Printers that are almost as tall as the room itself. \n To the East is the door that leads back into [Hallway - Section 2]")
    
    def fancyDes():
        print("[3D Printing Lab] \n The bright yellow sun is still beaming in through the tall, wall length windows. \n At the other end of the room, the massive 3D Printers are still slowly printing away, working on their current task. \n In the clear plastic bins below each table, I notice all the differently colored discarded projects; when I first came in here I could have sworn all these pieces were gray… \n To the East is [Hallway - Section 2]")

class CreatorOffice:
    def basicDes():
        print("[Creator's Office] \n Upon entering the room, a wave of familiarity overloads my thought process. This room feels similar to the room I've woken up in, but looks nothing alike. \n There are cupboards and shelves that line the walls of the room; they're filled with everything from scrap metal, gears, wires, and a multitude of snack foods. \n To my left is a tall bookshelf with a vent beside it.\n There is a large wooden desk in the middle of the room, on it is a pair of large monitors and a computer tower with a soft glow. \n To the East is [Hallway - Section 3]")
        
    def fancyDes():
        print("[Creator's Office] \n The Creator is still here doing her work. When I walk in, she looks at me with a smile, but reminds me that she's very busy with her work. \n The Creator's office is very unique compared to the other offices; is it because she's in a higher position, or perhaps she's spent more time making her room more unique than the other staff members? \n To the East is [Hallway - Section 3]")

class ServerRoom:
    def basicDes():
        print("[Server Room] \n There is nothing in this room except many large glass boxes, all containing flashing lights, and wires pouring in and out of the shelves of lights. \n One thing to note of this room is the amount of ventilation that's been designed; I reason that these large glass boxes must create a large amount of heat. \n To the East is the door that leads back into [Hallway - Section 4]")
    
    def fancyDes():
        print("[Server Room] \n The most boring room in the building; bland, colorless (minus the blinking red and green lights), and uninteresting. \n There are ribbons hanging from the vents above the room; they're flying in rythym to the air current. \n To the East is the door that leads back into [Hallway - Section 4] \n  I see a panel I haven't noticed before; There's a wire labeled Smoke Alarm.")
    
class OrigamiHeadOffice:
    def basicDes():
        print("[Abstract Solutions Office] \n The first thing I notice as I walk in is the vast amount of small animal figures that cover the room. \n Detailed paper recreations of animals are showcased on lit-up display shelves, sitting across counters, and covering the lone desk at the back of the room. \n Behind the desk is a large framed picture; I don’t think I've ever seen anything like this before, it looks similar to the foliage I saw outside. \n To the North is [Hallway - Section 4].")
    
    def fancyDes():
        print("[Abstract Solutions Office] \n Back to the room filled with 'Origami'. \n The paper recreations of animals are still on display on the lit-up display shelves. \n Seeing these recreations again, it's interesting to think that I value the way they look more now than I had when I first came, but nothing changed about them. \n The way each animal was created with its own specific paper, and that some bigger models have multiple, different coloured paper used to create it. \n To the North is [Hallway - Section 4]")
    
class Security:
    def basicDes():
        print("[Security] \n A room filled with monitors, all showing a different moving image on the screen. \n There are three employees sitting inside, matching uniform with the Security employee I cleaned up for on the way here.  \n They're all too busy watching the screen to take notice of me. \n There is a large glowing button with text on the other side of it. \n Past the guards and the monitors is a large window, it's facing towards a Security Checkpoint. \n To the North is [Hallway - Section 5].")
    
    def fancyDes():
        print("[Security] \n The security office is still staffed by three guards paying close attention to their monitors. \n Looking through the window, I see the Security Checkpoint with the slouched over guard.")
    
class Storage:
    def basicDes():
        print("[Storage] \n A storage room; there are countless shelves that make up the room carrying different items. \n There are parts that look like they're for the 3D Printers, different bottles of 'Printing Filament', and they're accompanied by other electronics such as wires, chargers, and laptops. \n On the other shelves are articles of clothing, they don't look similar to the uniform any of the employees wear; there are different hats, coats, and a dress. \n To the South is [Hallway - Section 6].")
    
    def fancyDes():
        print("[Storage] \n There are a lot more clothes in here than I originally remember. \n The clothes follow no particular style or color; it looks like there are clothes here from older periods of time, each having their own problems such as holes or missing buttons, while other pieces of clothing look like it's brand new. \n Some of these clothing look like they would fit me. \n To the South is [Hallway - Section 6].")

class Hallway1:
    def basicDes():
        print("[Hallway – Section 1] \n I'm in the Main Hallway inside of the large building complex. Written on the floors of the hallway is '#1' \n To the North is a door with a sign that reads: \n 'Robotics Testing Facility'. \n To the South is the rest of the Hallway, it appears to turn to the left at the end of the hall. \n To the West is a door with a sign that reads: \n 'Prototype Workshop'. \n To the East is the Guard Desk that I entered the building from. The Security Guard is at her desk.")
    
    def fancyDes():
        print("[Hallway – Section 1] \n I'm in the Main Hallway inside the large building complex. Written on the floors of the hallway is '#1' \n The #1 is written in a large, blocky looking font, painted all white. \n To the North is [Robotics Testing Facility]. \n To the South is [Hallway - Section 2]. \n To the West is [Prototype Workshop]. \n To the East is the [Security Checkpoint] I entered from.")

class Hallway2:
    def basicDes():
        print("[Hallway – Section 2] \n Written on the floor of this hallway is '#2'. \n To the North is [Hallway – Section 1]. \n To the South is [Hallway – Section 3]. \n To the West is a door with a sign that reads: \n 'Prototype Workshop' \n To the East is a door with a sign that reads: \n 'Programming Lab'")
    
    def fancyDes():
        print("[Hallway – Section 2] \n Written on the floor of this hallway is '#2'. \n To the North is [Hallway – Section 1]. \n To the South is [Hallway – Section 3]. \n To the West is [Prototype Workshop]. \n To the East is [Programming Lab].")
        
class Hallway3:
    def basicDes():
        print("[Hallway – Section 3] \n Written on the floor of this hallway is '#3'. \n To the North is [Hallway – Section #2]. \n To the South is [Hallway – Section #4]. \n To the West is a door with a sign that reads: \n Chief Operating Officer – Robotics \n Cordelia Weaver'. \n To the East is a door with a sign that reads: \n 'Head of Construction \n George Edifice'.")
    
    def fancyDes():
        print("[Hallway – Section 3] \n Written on the floor of this hallway is '#3'. \n To the North is [Hallway – Section #2]. \n To the South is [Hallway – Section #4]. \n To the West is [Chief Operating Officer – Robotics] \n To the East is [Head of Construction]")
    
class Hallway4:
    def basicDes():
        print("[Hallway – Section 4] \n I've reached the corner for this hallway, written on the floor is '#4'. \n To the North is [Hallway – Section #3]. \n To the South is a door with a sign that reads: \n 'Head of Abstract Solutions \n Ori Yami'. \n To the West is a door that reads: \n 'Server Room'. \n To the East, I see the hallway extending. There are more doors along the hallway, and it appears that the hallway turns another time to the right.")
    
    def fancyDes():
        print("[Hallway - Section 4] \n I've reached the corner for this hallway, written on the floor is '#4'. \n To the North is [Hallway – Section #3]. \n To the South is [Head of Abstract Solutions]. \n To the West is [Server Room]. \n To the East is [Hallway - Section 5].")

class Hallway5:
    def basicDes():
        print("[Hallway – Section 5] \n To the South is a door with a sign that reads: \n 'Security Office' \n To the West is [Hallway – Section #4]. \n To the East is [Hallway – Section #5].")
    
    def fancyDes():
        print("[Hallway – Section 5] \n To the South is [Security Office]. \n To the West is [Hallway – Section #4]. \n To the East is [Hallway – Section #5].")
    
class Hallway6:
    def basicDes():
        print("[Hallway – Section 6] \n I've reached the other end of the Hallway. \n To the North is a door with a sign that reads: \n 'Lost and Found / Storage' \n To the South is another Guard Desk, similar to the one I saw earlier. There appears to be two Security Guards, both sitting behind the desk monitoring different sets of monitors. \n To the West is [Hallway – Section #5].")
    
    def fancyDes():
        print("[Hallway – Section 6] \n To the North is [Lost and Found / Storage]' \n To the South is [Security Checkpoint] \n To the West is [Hallway – Section #5].")
    
class Exit:
    def basicDes():
        print("[Building Exit] \n Identical to the other Security Checkpoint I walked through earlier, there is a guard desk between two metal gates, with a set of monitors displaying different moving images. \n There is a guard sitting at the desk, sitting in a slouched position and appears to be watching the screens. There's also a window facing out from the Security Office. \n To the North is [Hallway - Section 6].")
    
    def fancyDes():
        print("[Building Exit] \n The Security Checkpoint still sits here with the slouched over guard sitting at the desk. \n He's in the same position as when I had seen him earlier.. Are the monitors turned off? \n To the North is [Hallway - Section 6].")
