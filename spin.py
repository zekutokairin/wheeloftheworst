#!/usr/bin/env python

import os
import sys
import platform

from config import *

BAKPATH = None

if platform.system() == "Darwin":
    MOVIEPATH = os.path.join("Contents","UE4","SuperVHS","Content","Movies")
    PATH = os.path.join(MACPATH,MOVIEPATH)

elif platform.system() == "Windows":
    MOVIEPATH = os.path.join("SuperVHS","Content","Movies")
    PATH = os.path.join(WINPATH,MOVIEPATH)

else:
    raise Exception("Unsupported OS: %s" % platform.system())


BAKPATH = os.path.join(PATH, "backup")
if not os.path.exists(BAKPATH):
    os.mkdir(BAKPATH)
    # TODO: Move movies over
    raise NotImplementedError

# Takes a list of full paths to movie files
# Copies up to 14 of them into the SuperVHS movie folder
def spinTheWheel(movie_entries):
    for entry in movie_entries:
        # TODO cp entry
        pass

if __name__ == "__main__":
    print(PATH)
    print(os.listdir(PATH))

    args = sys.argv[1:]
    # TODO: Clean out movie directory before 
    wheeldir = 
    print(args)

