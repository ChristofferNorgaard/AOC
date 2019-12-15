loc = {'a' : 8, 'b' : -2, 'c' : 2, 'd':-5}
speed = {'a' : 0, 'b': 0, 'c': 0, 'd': 0}
from collections import Counter
chck = str(sorted(loc.items(), key=lambda x: x[1], reverse=False))
i = 0
last_val = ''
print(chck, str(sorted(loc.items(), key=lambda x: x[1], reverse=False)))
while chck != str(sorted(loc.items(), key=lambda x: x[1], reverse=False)) or i == 0:
    i += 1
    last_val = ''
    last_key = ''
    if i > 1000000000:
        print('problem')
        break
    lst = sorted(loc.items(), key=lambda x: x[1], reverse=False)
    counter = Counter(x[0] for x in lst)
    constructer = [0, 0, 0, 0]
    for k, v in lst:
        speed[k] += (sum(1 if e[1] > v else 0 for e in lst)) -(sum(1 if e[1] < v else 0 for e in lst))
    #print(speed)
    for k, v in lst:
        loc[k] += speed[k]
    #print(sorted(loc.items(), key=lambda x: x[0], reverse=False))
    #print(speed)
    #input()

print(i)