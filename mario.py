# mario.py
# Copyright 2020 Lu Neder
#
# This work may be distributed and/or modified under the
# conditions of the LaTeX Project Public License, either version 1.3
# of this license or (at your option) any later version.
# The latest version of this license is in
#   http://www.latex-project.org/lppl.txt
# and version 1.3 or later is part of all distributions of LaTeX
# version 2005/12/01 or later.
#
# This work has the LPPL maintenance status `maintained'.
#
# The Current Maintainer of this work is Lu Neder.
#
# This work consists of the files mario.py and README.md.


import time
import playsound
import sys
import glob
import random as randomizer
from datetime import datetime

#Safe command lines args as args
args = str(sys.argv)

#Asks how many seconds between plays and saves answer as t (unless arg --help is passed)
if (args.__contains__("--help")):
    random = "help"
else:
    t = int(input("How many seconds between plays? -> "))
    print(t)

#Checks if random mode is active and ask for directory, file path or shows help
if (args.__contains__("--random")):
    random = "true"
    print("Random mode: will randomly play a different audio file from the specified directory every " + str(t) + " seconds")
    d = input("Directory path to get files from -> ")
    print(d)
elif (args.__contains__("--help")):
    print("Help mode")
    print("--help: Help mode: Displays this message")
    print("--random: Random mode: will randomly play a different audio file from a specific directory every t seconds")
    print("no args: Normal mode: will play a specific audio file every t seconds")
else:
    random = "false"
    print("Normal mode: will play a specific audio file every " + str(t) + " seconds")
    f = input("File path -> ")
    print(f)

#Set played times to 0
n = 0

#Runs the selected mode, depending on the args
if random == "false":
    #A while loop
    while True:
        #Play the sound
        playsound.playsound(f)
        #Update the times played and print it. Get the time and print it.
        n = n + 1
        v = str(n)
        agr = datetime.now()
        ptime = agr.strftime("%H:%M:%S")
        print("Played " + v + " times - " + ptime)
        #Waits t seconds
        time.sleep(t)
elif random == "true":
    #A while loop
    while True:
        #Get all files in the directory (and save as all_files), choose a random one (and save as file) and print the choosen file's name
        all_files = glob.glob(d)
        file = randomizer.choice(all_files)
        print("Playing " + str(file))
        #Play the sound
        playsound.playsound(file)
        #Update the times played and print it. Get the time and print it.
        n = n + 1
        v = str(n)
        agr = datetime.now()
        ptime = agr.strftime("%H:%M:%S")
        print("Played " + v + " times - " + ptime)
        #Waits t seconds
        time.sleep(t)
elif random == "help":
    print(" ") #Print an empty line, since help was already shown
else:
    print("something went wrong") #Mario is made in a way that the variable random will always be either true, false or help. Because of this, Mario should never arrive at this else and if it does it's because something went very wrong.
