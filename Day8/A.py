a = input()
print(len(a))
l = 25*6;
b = [a[i: i + l] for i in range(0, len(a), l)]
res = ['-'] * l;
print(len(b[0]))
for i in range(l):
    print(i)
    for e in b:
        #print(i)
        res[i] = e[i];
        #print("e[i]")
        if(e[i] != '2'):
            break
#print(res)
for i in range(0, len(res), 25):
    print(''.join(res[i:i+25]))