#!/usr/bin/env python

import os
import platform

WINPATH = "C:\\Users\\user\\apps\\SuperVHS_v1.2-win"
MACPATH = "/Users/user/Games/SuperVHS_v1.2-mac/SuperVHS.app"

if platform.system() == "Darwin":
    MOVIEPATH = os.path.join("Contents","UE4","SuperVHS","Content","Movies")
    PATH = os.path.join(MACPATH,MOVIEPATH)

elif platform.system() == "Windows":
    MOVIEPATH = os.path.join("SuperVHS","Content","Movies")
    PATH = os.path.join(WINPATH,MOVIEPATH)

else:
    raise Exception("Unsupported OS: %s" % platform.system())

if not os.path.exists(os.path.join(PATH,"backup")):
    # TODO: Create it
    # TODO: Move movies over
    raise NotImplementedError

import code
#code.interact(local=locals())

MOVIES = ["RLMTV_DD1.mov",
"RLMTV_DD2.mov",
"RLMTV_FF1.mov",
"RLMTV_FF2.mov",
"RLMTV_Hawaii1.mov",
"RLMTV_Hawaii2.mov",
"RLMTV_Ishtar.mov",
"RLMTV_MacMe.mov",
"RLMTV_NightCourt.mov",
"RLMTV_SWHS1.mov",
"RLMTV_SWHS2.mov",
"RLMTV_Sasquatch.mov",
"RLMTV_Shimmy.mov",
"RLMTV_Twisted1.mov",
"RLMTV_Twisted2.mov"]

print(PATH)
print(os.listdir(PATH))

