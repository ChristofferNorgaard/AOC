inp = -1
moons = []
while True:
    inp = input()
    if inp == "" : break
    inp =  [e.split('=') for e in inp[1:-1].replace(" ", "").split(',')]
    inp = tuple([int(e[1]) for e in inp])
    moons.append((inp, (0,0,0))

print(moons)
while True:
    i = 0
    for i in range(5)
        for j in range(5 - i):
            print(j)