import math;
stdp= input().split(',')
def program(ai, bi):
    p = [int(x) for x in list(stdp)]
    i = 0;
    #p[1] = ai
    #p[2] = bi
    #print("mmmm")
    while(True):
        if(p[i] == 99):
            break;
        elif(p[i]%10 == 1):
            command = math.floor(p[i]/100)
            command = str(command)
            if(command[-1:] == "0"):
                a = p[p[i+1]]
            elif(command[-1:] == "1"):
                a = p[i+1]
            else:
                print("input was :" + str(command[:1]) + "i was " + str(i))
                a = p[p[i+1]]
            if(command[-2:-1] == "0"):
                b = p[p[i+2]]
            elif(command[-2:-1] == "1"):
                b = p[i+2]
            else:
                print("input was :" + str(command[-2:-1]) + "i was " + str(i))
                b = p[p[i+2]]
            c = p[i+3]
            print("Add " + str(a) + "+" + str(b))
            p[c] = a + b
            n = 4;
        elif(p[i]%10 == 2):
            command = math.floor(p[i]/100)
            command = str(command)
            if(command[-1:] == "0"):
                #print("The first was pos")
                a = p[p[i+1]]
            elif(command[-1:] == "1"):
                #print("The first was abs")
                a = p[i+1]
            else:
                a = p[p[i+1]]
                print("input was :" + str(command[:1] + "i was " + str(i)))
            if(command[-2:-1] == "0"):
                b = p[p[i+2]]
            elif(command[-2:-1] == "1"):
                b = p[i+2]
            else:
                print("input was :" + str(command[:1])+ "i was " + str(i))
                b = p[p[i+2]]
            c = p[i+3]
            #print("addres line is "+ str(c))
            print("Mul" + str(a) + "*" + str(b))
            p[c] = a * b
            print("result is " + str(p[c]))
            n = 4;
        elif(p[i] == 3):
            p[p[i+1]] = int(input("The computer has requested input: "))
            n = 2;
        elif(p[i]%10 == 4):
            command = math.floor(p[i]/100)
            command = str(command)
            if(command[-1:] == "0"):
                print(p[p[i+1]])
            elif(command[-1:] == "1"):
                print(p[i+1])
            #print(p[p[i+1]])
            n = 2;
        elif(p[i]%10 == 5):
            command = math.floor(p[i]/100)
            command = str(command)
            if(command[-1:] == "0"):
                a = p[p[i+1]]
            elif(command[-1:] == "1"):
                a = p[i+1]
            else:
                print("input was :" + str(command[:1]) + "i was " + str(i))
                a = p[p[i+1]]
            if(command[-2:-1] == "0"):
                b = p[p[i+2]]
            elif(command[-2:-1] == "1"):
                b = p[i+2]
            else:
                print("input was :" + str(command[-2:-1]) + "i was " + str(i))
                b = p[p[i+2]]
            if(a != 0):
                i = b;
                n = 0;
            else:
                n = 3;
        elif(p[i]%10 == 6):
            command = math.floor(p[i]/100)
            command = str(command)
            if(command[-1:] == "0"):
                a = p[p[i+1]]
            elif(command[-1:] == "1"):
                a = p[i+1]
            else:
                print("input was :" + str(command[:1]) + "i was " + str(i))
                a = p[p[i+1]]
            if(command[-2:-1] == "0"):
                b = p[p[i+2]]
            elif(command[-2:-1] == "1"):
                b = p[i+2]
            else:
                print("input was :" + str(command[-2:-1]) + "i was " + str(i))
                b = p[p[i+2]]
            if(a == 0):
                i = b;
                n = 0;
            else:
                n = 3;
        elif(p[i]%10 == 7):
            command = math.floor(p[i]/100)
            command = str(command)
            if(command[-1:] == "0"):
                a = p[p[i+1]]
            elif(command[-1:] == "1"):
                a = p[i+1]
            else:
                print("input was :" + str(command[:1]) + "i was " + str(i))
                a = p[p[i+1]]
            if(command[-2:-1] == "0"):
                b = p[p[i+2]]
            elif(command[-2:-1] == "1"):
                b = p[i+2]
            else:
                print("input was :" + str(command[-2:-1]) + "i was " + str(i))
                b = p[p[i+2]]
            c = p[i+3]
            if(a < b):
                p[c] = 1;
            else:
                p[c] = 0;
            n = 4;
        elif(p[i]%10 == 8):
            command = math.floor(p[i]/100)
            command = str(command)
            if(command[-1:] == "0"):
                a = p[p[i+1]]
            elif(command[-1:] == "1"):
                a = p[i+1]
            else:
                print("input was :" + str(command[:1]) + "i was " + str(i))
                a = p[p[i+1]]
            if(command[-2:-1] == "0"):
                b = p[p[i+2]]
            elif(command[-2:-1] == "1"):
                b = p[i+2]
            else:
                print("input was :" + str(command[-2:-1]) + "i was " + str(i))
                b = p[p[i+2]]
            c = p[i+3]
            if(a == b):
                p[c] = 1;
            else:
                p[c] = 0;
            n = 4;
        else:
            print("something went wrong here")
            break;
        i += n;
    #return p[0];
    return(" ")
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