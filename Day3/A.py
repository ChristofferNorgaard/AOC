line1 = input().split(',')
line2 = input().split(',')
lines = {};
intersections = []; 
x, y = 0, 0
steps = 0
for c in line1:
    com = c[:1]
    num = int(c[1:])
    yi = 0
    xi = 0
    if(com == "R"):
        yi = 0;
        xi = 1;
    elif(com == "L"):
        yi = 0;
        xi = -1
    elif(com == "U"):
        yi = 1;
        xi = 0;
    elif(com == "D"):
        yi = -1;
        xi = 0;
    else:
        print("Error")
        break;
    for i in range(num):
        steps += 1
        y += yi;
        x += xi;
        lines[str([x, y])] = steps;
        
x, y = 0, 0
steps = 0
for c in line2:
    com = c[:1]
    num = int(c[1:])
    yi = 0
    xi = 0
    if(com == "R"):
        yi = 0;
        xi = 1;
    elif(com == "L"):
        yi = 0;
        xi = -1
    elif(com == "U"):
        yi = 1;
        xi = 0;
    elif(com == "D"):
        yi = -1;
        xi = 0;
    else:
        print("Error")
        break;
    for i in range(num):
        steps += 1
        y += yi;
        x += xi;
        lin = lines.get(str([x, y]))
        if(lin):
            
            #print("intersection at " + str(x) + " " + str(y))
            intersections.append(steps + lin)
            #lines[str([x, y])] = -1;
        else:
            pass
            #lines[str([x, y])] = 2;

print(min(intersections))
