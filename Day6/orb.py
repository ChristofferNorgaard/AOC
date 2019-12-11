elements = []
sanp = []
youp = []
con = {}
y = 0
s = 0
while(True):
    
    a = input().split(")") 
    if(a[0] == "b"):
        break
    else:
        elements.append(a)
    if(a[1] == "YOU"):
        y = elements.index(a)
    if(a[1] == "SAN"):
        s = elements.index(a)
    for i in a:
        if(not i in con.keys()):
            con[i] = 0;
def se(a, b):
    path = []
    path.append(b)
    for i in elements:
        if(i[1] == a):
            path += se(i[0], i[1])
            break
    return path
#print(len(elements))
#print(start)
youp = se(elements[y][0], elements[y][1])
sanp = se(elements[s][0], elements[s][1])
inds = 0;
indj = 0
for i in youp:
    if(i in sanp):
        inds = sanp.index(i);
        indj = youp.index(i);
        print("Element is" + i)
        break
print(inds-1)
print(indj-1)
print(indj-1 + inds-1)
