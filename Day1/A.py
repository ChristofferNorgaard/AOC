import math
allsum = 0
while(True):
    try:
        a = int(input())
    except:
        break;
    a = math.floor(a / 3) -2
    allsum += a;
    while(True):
        a = math.floor(a / 3) - 2
        if(a < 0):
            break;
        else:
            allsum += a;
    
print(allsum)