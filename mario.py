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
from pydub import AudioSegment
from pydub.playback import play

#Asks how many seconds between plays and saves answer as t
t = int(input("How many seconds between plays? -> "))
print(t)


a = input("File path -> ")
f = AudioSegment.from_wav(a)


while True:
    play(f)
    time.sleep(t)
