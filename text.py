# -*- coding: utf-8 -*-
"""
Text
"""

def intro():
    print("I find myself in the dark corner of a room, wires connected to multiple locations on your body. As I wake up, the wires disconnect automatically. I have a User's Guide.")

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