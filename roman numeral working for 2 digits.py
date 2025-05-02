n=input()
s=''
s1=n[0]
s2=n[1]
if s1 in ['1','2','3']:
    s+='X'*int(s1)
elif s1 == '4':
    s+='XL'
elif s1 == '9':
    s+='XC'
else:
    s+='L'+'X'*(int(s1)-5)

if s2 in ['1','2','3']:
    s+='I'*int(s2)
elif s2 == '4':
    s+='IV'
elif s2 == '9':
    s+='IX'
elif s2 == '0':
    pass
else:
    s+='V'+'I'*(int(s2)-5)
    
print(s)