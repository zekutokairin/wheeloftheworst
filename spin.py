#!/usr/bin/env python

import os
import platform

# Path in the SuperVHS directory
WINPATH = "C:\\Users\\user\\apps\\SuperVHS_v1.2-win"
# Path within the .app file
MACPATH = "/Contents/UE4/SuperVHS/Content/Movies"

MOVIEPATH = os.path.join("SuperVHS","Content","Movies")

if platform.system() == "Darwin":
    PATH = os.path.join(MACPATH,MOVIEPATH)

elif platform.system() == "Windows":
    PATH = os.path.join(WINPATH,MOVIEPATH)

else:
    raise Exception("Unsupported OS: %s" % platform.system())


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

print("Hello world") 
print(PATH)

