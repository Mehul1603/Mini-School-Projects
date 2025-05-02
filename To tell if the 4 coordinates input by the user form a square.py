#To tell if the 4 coordinates input by the user form a square

c = []

for i in range(4):
    a = eval(input("Enter the coordinates in the form of tuple (x-coordinate,y-coordinate): "))
    c += [a]
    
diag = []    

for i in range(4):
    x = c[i][0]
    y = c[i][1]
    dist = []
    for j in range(4):
        if j != i:
            x1 = c[j][0]
            y1 = c[j][1]
            d = ((x-x1)**2 + (y-y1)**2)**(1/2)
            dist += [d]
    dist.sort()
    if dist[0]==dist[1]:
        diag += [dist[2]]
    else:
        print("It is not a square")
        break
else:
    for i in range(1,4):
        if diag[0] != diag[i]:
            print('It is not a square')
            break
    else:
        
        print('It is a square')