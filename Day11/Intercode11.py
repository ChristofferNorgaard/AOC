import math
add = lambda a, b: a+b
mul = lambda a, b: a*b
jump_if_true = lambda a, b: b if a != 0 else None
jump_if_false = lambda a, b: b if a == 0 else None
less_than = lambda a, b: 1 if a < b else 0
equals = lambda a, b: 1 if a == b else 0
comm_dict = {
    1 : add,
    2 : mul,
    5 : jump_if_true,
    6 : jump_if_false,
    7 : less_than,
    8 : equals
}
shc_dict = {1:4, 2:4, 3: 2, 4: 2, 5 : 3, 6: 3, 7: 4, 8: 4, 9: 2, 99: 1}
def run_com(com, mem, rel, inp=None):
    exe = com[0] % 100
    mod = (math.floor(com[0] / 100))
    arg = com[1:]
    chn = None
    out = None
    pos = com[-1]
    modes = []
    for i in range(len(arg)):
        mode = int(mod%10); mod = mod/10
        modes.append(mode)
        if(mode == 0): arg[i] = mem[arg[i]]
        if(mode == 2):arg[i] = mem[arg[i] + rel]
    if(len(modes) > 0):
        if(modes[-1] == 2):
            pos += rel
    if(exe in [1, 2, 7, 8]):
        mem[pos] = comm_dict[exe](arg[0], arg[1])
    elif(exe in [5, 6]):
        chn = comm_dict[exe](arg[0], arg[1])
    elif(exe == 3):
        #print('mod', arg)
        if(inp != None and math.floor(com[0] / 100) == 0):
            mem[pos] = int(inp)
        elif(inp != None and math.floor(com[0] / 100) == 2):
            mem[pos] = int(inp)
        else: return (('INP_REQ'))
    elif(exe == 4):
        out = arg[0]
    elif(exe == 9):
        rel += arg[0]
    elif(exe == 99):
        return(('BRAKE'))
    else:
        print("something wrong here")
        return(('ERROR'))
    return((mem, rel, out, chn))
with open('program.txt', 'r') as file:
    data = [int(x) for x in file.read().replace('\n', '').split(',')]
mem = data + [0 for i in range(1000000)]
map_ = {}
loc = (0, 0)
get_color = lambda x, y: 1 if map_[(x, y)] == 1 else 0
point = 0
rel = 0;
out_mode = 'c'
locations = []
count = 0
rot = 0
rotations = [(0, -1), (1, 0), (0, 1), (-1, 0)]
map_[loc] = 1
while True:
    count += 1
    try:
        sch = shc_dict[mem[point]%100]
    except:
        print(point)
        break
    com = mem[point : point+sch]
    res = run_com(com, mem, rel)
    if(res == ('INP_REQ')):
        try:
            inp = get_color(loc[0], loc[1])
        except KeyError:
            inp = 0
        res = run_com(com, mem, rel, inp)
    elif(res == ('BRAKE')):
        print('BRAKE')
        break
    elif(res == ('ERROR')):
        print('ERROR')
        raise ArithmeticError(com)
    mem = res[0]; rel = res[1]; out = res[2]; chn = res[3]
    if(out != None):
        if(out_mode == 'c'):
            map_[loc] = out
            if(loc not in locations): locations.append(loc)
            print('loc', loc, 'map', map_[loc])
            out_mode = 'r'
        else:
            trn = 1 if out == 1 else -1
            rot = rot+ trn if 0 <=  rot + trn < 4 else rot + trn - 4 if 4 <= rot + trn else 4 + rot + trn
            print(rot, trn)
            loc = (loc[0] + rotations[rot][0], loc[1] + rotations[rot][1])
            print('rot', rot)
            out_mode = 'c'
        if(out == 'P'):
            print(com)
            break
    if(chn != None):
        point = chn
    else:
        point += sch
print(len(map_.keys()), len(locations), count)
for i in range(100):
    stringprint = ""
    for j in range(100):
        if((j, i) in map_.keys()):
            if(map_[(j, i)] == 1):
                stringprint += "#"
            else:
                stringprint += " "
        else:
            stringprint += " "
    print(stringprint)