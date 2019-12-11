import math
import pprint
from operator import itemgetter
mapi = []
line = 0
center = (17, 22)
angles = []
#Point(x=17, y=22)
while True:
    a = input()
    if a == "": break
    for i in range(len(a)):
        if a[i] == "#":
            x = float(center[0] - i)
            y = float(center[1] - line)
            r = math.hypot(x, y)
            th = math.atan2(y, x) - math.atan2(1, 0)
            mapi.append((th, r, x*-1, y*-1))
            if(th not in angles): angles.append(th)
    line += 1
angles.sort()
#print(angles)
sss = []
i = 0
while (angles[i] < 0): i+= 1
while True:
    if(len(mapi) < 1): break
    an = angles[i]
    matches = [x for x in mapi if x[0] == an]
    if(len(matches) > 0):
        a = min(matches, key=itemgetter(1))
        mapi.remove(a)
        real_x = a[2] + center[0]
        real_y = a[3] + center[1]

        sss.append((real_x, real_y))
    i += 1
    if not i < len(angles): i = 0
print(sss[199])