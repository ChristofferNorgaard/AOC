inp = -1
import pprint
moons = []
while True:
    inp = input()
    if inp == "" : break
    inp =  [e.split('=') for e in inp[1:-1].replace(" ", "").split(',')]
    inp = [int(e[1]) for e in inp]
    moons.append((inp, [0,0,0]))
x = str([x[0][0] for x in moons])
y = str([x[0][1] for x in moons])
z = str([x[0][2] for x in moons])
print(moons)
count = 0
while True:
    count += 1
    #energy = 0
    for i in range(len(moons)):
        master = i
        for j in range(len(moons) - i-1):
            slave = j+i+1
            for k in range(3):
                vel_s = -1 if moons[slave][0][k] > moons[master][0][k] else 1 if moons[slave][0][k] < moons[master][0][k] else 0
                vel_mas = vel_s*-1
                moons[master][1][k] += vel_mas; moons[slave][1][k] += vel_s;
        for k in range(3):
            moons[master][0][k] += moons[master][1][k]
        if(str([x[0][0] for x in moons]) == x): print('x', count, moons, x); input()
        if(str([x[0][1] for x in moons]) == y): print('y', count); input()
        if(str([x[0][2] for x in moons]) == z): print('z', count); input()
pprint.pprint(moons)