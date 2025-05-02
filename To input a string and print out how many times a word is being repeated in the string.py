#To input a string and print out how many times a word is being repeated in the string

def pos(val,l):
    for i in range(len(l)):
        if val == l[i]:
            return i
            break

a = input('Enter a string: ')
a += ' '
w = []
x=0
for i in range(len(a)):
    if a[i] == ' ':
        w += [a[x:i]]
        x = i+1

m = []
for i in range(len(w)):
    k = w.pop(i)
    if k in w and k != 0:
        m += [(k,w.count(k)+1)]
        for j in range(w.count(k)):
            o = pos(k,w)
            w.remove(k)
            w.insert(o,0)
    elif k not in w and k != 0:
        m += [(k,1)]
    w.insert(i,0)

for z in m:
    a,b=z
    if b == 1:    
        print(a,':',b,'time')
    else:
        print(a,':',b,'times')
    
#Test input: hello how are you how how you are are are are hello not why in