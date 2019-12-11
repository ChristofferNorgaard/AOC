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
def run_com(com, mem, rel, inp=False):
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
        print('mod', arg)
        if(inp and math.floor(com[0] / 100) == 0):
            mem[pos] = int(inp)
        elif(inp and math.floor(com[0] / 100) == 2):
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
point = 0
rel = 0;
while True:
    sch = shc_dict[mem[point]%100]
    com = mem[point : point+sch]
    res = run_com(com, mem, rel)
    if(res == ('INP_REQ')):
        inp = input('e: ')
        res = run_com(com, mem, rel, inp)
    elif(res == ('BRAKE')):
        print('BRAKE')
        break
    elif(res == ('ERROR')):
        print('ERROR')
        print(com)
        break
    mem = res[0]; rel = res[1]; out = res[2]; chn = res[3]
    if(out != None):
        print(out)
        if(out == 'P'):
            print(com)
    if(chn != None):
        point = chn
    else:
        point += sch