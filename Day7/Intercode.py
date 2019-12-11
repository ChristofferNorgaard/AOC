import math
with open('program.txt', 'r') as file:
    data = [int(x) for x in file.read().replace('\n', '').split(',')]
shc_dict = {1:4, 2:4, 3: 2, 4: 2, 5 : 3, 6: 3, 7: 4, 8: 4, 9: 2, 99: 1}
pos = {1: 1, 2: 1, 3: 1, 4: 0, 5: 1, 6: 0, 7: 1, 8: 1, 9: 0, 99 : 0}
def int_code(mem, com, rel, inp=''):
    sch = 0
    #input handeling
    if(com[0] < 100):
        #print('no')
        for i in range(len(com) -1 - pos[com[0]]):
            com[i+1] = mem[com[i+1]]
    else:
        remander = (str(math.floor(com[0]/100)))[::-1]
        for i in range(len(remander) - len(com) - 2):
            #print("added digit" + str(remander))
            remander += '0'
        #print(len(remander))
        for e in range(len(remander)):
            if(remander[e] == '0'):
                #print(' zerooo')
                com[e+1] = mem[com[e+1]]
            elif(remander[e] == '1'):
                #print('one one a day at' + str(com[0]))
                pass
            elif(remander == '2'):
                com[e+1] = mem[com[e+1]+rel]
                #print('rel is ok')
            else:
                #print(remander[e])
                pass
    com[0] = com[0]%100
    if(com[0] == 99):
        return(('BRAKE', 0, 0));
    elif(com[0] == 1):
        mem[com[3]] = com[1] + com[2]
        return(('ADD', mem, sch))
    elif(com[0] == 2):
        mem[com[3]] = com[1] * com[2]
        return(('MUL', mem, sch))
    elif(com[0] == 3):
        if(inp == ''):
            return(('REQUEST_INPUT'))
        else:
            mem[com[1]] = int(input("e: ")) #command[(cur, 'inp')]
            return(('INPUT' + str(inp), mem, sch))
    elif(com[0] == 4):
        return(('PRINT', mem, sch, com[1]))
    elif(com[0] == 5):
        if(com[1] != 0): sch = com[2];
        else: 
            sch = 'bu'
        return(('COMPARE_JUMP_5', mem, sch))
    elif(com[0] == 6):
        if(com[1] == 0): sch = com[2];
        else: 
            sch = 'bu'
        return(('COMPARE_JUMP_6', mem, sch))
    elif(com[0] == 7):
        mem[com[3]] = int(com[1] < com[2]);
        return(('COMPARE_WRITE_7', mem, sch))
    elif(com[0] == 8):
        mem[com[3]] = int(com[1] == com[2]);
        return(('COMPARE_WRITE_8', mem, sch))
    elif(com[0] == 9):
        return(('CHANGE_REL', mem, sch, rel+com[1]))
    else:
        print('problem' + str(com[0]))
#print(int_code([1002,4,3,4,33], [1002,4,3,4]))
mem = data + [0 for _ in range(1000)]
point =0;
rel = 0;
sch = shc_dict[mem[point]%100]
point =0;
rel = 0;
sch = shc_dict[mem[point]%100]
while True:
    try:
        sch = shc_dict[mem[point]%100]
    except IndexError as e:
        print(e)
        print(point)
        break
    com = mem[point : point+sch]
    res = int_code(mem, com, rel)
    if(res[0] == 'BRAKE'):
        print('BRAKE')
        break
    elif(res[0] == 'PRINT'):
        print(str(res[3]))
    elif(res == 'REQUEST_INPUT'):
        inpt = input('input needed: ')
        res = int_code(mem, com, rel, inpt)
    elif(res[0] == 'CHANGE_REL'):

        rel = res[3]
    elif('COMPARE_JUMP' in res[0]):
        if(res[2] != 'bu'):
            point = res[2] - sch
    else:
        pass
    mem = res[1]
    point += sch;
    