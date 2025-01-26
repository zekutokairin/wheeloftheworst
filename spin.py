#!/usr/bin/env python

import os
import sys
import platform
import shutil
import random

from config import *

BAKPATH = None

def usage():
    print("./spin.py <Directory with movies>")

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
        print("Copying in movie: %s" % entry)
        # TODO cp entry
        # shutil.copy(entry, target)

if __name__ == "__main__":
    print(PATH)
    print(os.listdir(PATH))

    try:
        args = sys.argv[1:]
        sourcemovie_dir = args[0]
    except IndexError:
        sys.exit(usage)

    if os.path.isdir(sourcemovie_dir):
        # It's a directory, pass in the files
        # TODO make sure to use full paths
        movies = os.listdir(sourcemovie_dir)
        fullpath_movies = []
        random.seed()
        for movie in movies:
            if os.path.isdir(movie):
                continue
            else:
                fullpath_movies.append(os.path.join(sourcemovie_dir,movie))
        random.shuffle(fullpath_movies)
        spinTheWheel(movies)

    # TODO: Clean out movie directory before copying new ones in
    #wheeldir = 
    print(args)

