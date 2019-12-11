
ranin = [int(x) for x in input().split("-")]
re = 0;
for i in range(ranin[0], ranin[1]):
    strin = str(i)
    last = " "
    lastlast = " "
    ok = False;
    rep = 0;
    for s in (strin):
        if(not last <= s):
            #print("error")
            ok = False;
            rep = 0;
            break  
        elif(s == last):
            #print("is")
            rep = rep + 1;
            #print(rep)
        else:
            #print(rep)
            if(rep == 1):
                ok = True;
            rep = 0;

        last = s
        
    if(rep == 1):
        ok = True;
        
    if(ok):
        re += 1;

print(re);
'''
re = 0;
strin = input() + " "
last = " "
ok = False
rep = 0;
for s in (strin):
    if(not last <= s):
        #print("error")
        ok = False;
        break  
    elif(s == last):
        #print("is")
        rep = rep + 1;
        #print(rep)
    else:
        #print(rep)
        if(rep == 1):
            ok = True;
        rep = 0;

    last = s
        
if(rep == 1):
    ok = True;
    

if(ok ):
    print(ok)
    re += 1;
print(re)
'''