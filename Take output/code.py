
f=open('a.txt','r')
p=f.read()

l=p.split()
print(l)

for i in range(len(l)):
    l[i]=int(l[i])
print(l)
f.close()

f=open('a.txt','w')
f.write(str(l))
f.close()
