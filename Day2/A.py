stdp= input().split(',')
def program(ai, bi):
    p = [int(x) for x in list(stdp)]
    i = 0;
    p[1] = ai
    p[2] = bi
    #print("mmmm")
    while(True):
        if(p[i] == 99):
            break;
        elif(p[i] == 1):
            a = p[i+1]
            b = p[i+2]
            c = p[i+3]
            p[c] = p[a] + p[b]
        elif(p[i] == 2):
            a = p[i+1]
            b = p[i+2]
            c = p[i+3]
            p[c] = p[a] * p[b]
        else:
            print("something went wrong here")
            break;
        i += 4;
    return p[0];
    '''
    result = []
    for e in p:
        if(len(result) >= 4):
            print(", ".join([str(x) for x in result]))
            result = []
        
        result.append(e)

    print(", ".join([str(x) for x in result]))
    

for i in range(1000):
    for j in range(1000):
        try:
            if(program(i, j) == 19690720):
                print(str(i) + " " + str(j))
                break;
        except:
            pass;
'''
print(program(42, 59))