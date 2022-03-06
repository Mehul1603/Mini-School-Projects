a = input("Enter the string: ")
s = a.split(' ')
l = len(s)
m=0
g="There is no palindrome in the string"
for i in range(0,l):
    for j in range(0,len(s[i])):
        x=0
        if s[i]==s[i][::-1]:
            x=1
    if x==1:
        if m<len(s[i]):
            m=len(s[i])
            g=s[i]
        elif m==len(s[i]):
            g=g,s[i]
print(g)