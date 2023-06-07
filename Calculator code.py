e=input()
e=list(e)


def solve(s):
    ops=['+','-','*','/']
    for i in range(len(s)):
        if s[i] in ops:
            continue
        else:
            s[i]=float(s[i])

    while '/' in s:
        for j in range(len(s)):
            if s[j]=='/':
                p=s.pop(j-1)
                q=s.pop(j)
                del s[j-1]
                x=p/q
                s.insert(j-1,x)
                break
    while '*' in s:
        for j in range(len(s)):
            if s[j]=='*':
                p=s.pop(j-1)
                q=s.pop(j)
                del s[j-1]
                x=p*q
                s.insert(j-1,x)
                break
    while '+' in s:
        for j in range(len(s)):
            if s[j]=='+':
                p=s.pop(j-1)
                q=s.pop(j)
                del s[j-1]
                x=p+q
                s.insert(j-1,x)
                break
    while '-' in s:
        for j in range(len(s)):
            if s[j]=='-':
                p=s.pop(j-1)
                q=s.pop(j)
                del s[j-1]
                x=p-q
                s.insert(j-1,x)
                break
    return s

i=0
while i<len(e):
    if e[i]=='(':
        del e[i]
        p=[]
        for j in range(i,len(e)):
            if e[i]==')':
                del e[i]
                break
            else:
                p.append(e[i])
                del e[i]
        p=solve(p)
        e.insert(i,p[0])
        i+=len(p)-1
    i+=1
    
try:
    print(solve(e)[0])
except:
    print('error')

