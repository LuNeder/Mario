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

n = 0

if random == "false":
    while True:
        playsound.playsound(f)
        n = n + 1
        v = str(n)
        print("Played " + v + " times")
        time.sleep(t)
elif random == "true":
    while True:
        all_files = glob.glob(d)
        file = randomizer.choice(all_files)
        print("Playing " + str(file))
        playsound.playsound(file)
        n = n + 1
        v = str(n)
        print("Played " + v + " times")
        time.sleep(t)
elif random == "help":
    print(" ")
else:
    print("something went wrong")
