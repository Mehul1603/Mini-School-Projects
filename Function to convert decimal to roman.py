def roman(n):
    r = ''
    s = list(str(n))
    s.reverse()
    
    l = len(s)
    for i in range(l):
        h = int(s[i])
        c = h - 5
        
        if i == 0:
            if c<0 and c != -1:
                b = 'I'*c
            elif c == -1:
                b = 'IV'
            elif c == 4:
                b = 'IX'
            else:
                b = 'V'+'I'*c
            r = b + r
            continue
        
        elif i == 1:
            if c<0 and c != -1:
                b = 'X'*c
            elif c == -1:
                b = 'XL'
            elif c == 4:
                b = 'XC'
            else:
                b = 'L'+'X'*c
            r = b + r
            continue
        
        elif i == 2:
            if c<0 and c != -1:
                b = 'C'*c
            elif c == -1:
                b = 'CD'
            elif c == 4:
                b = 'CM'
            else:
                b = 'D'+'C'*c
            r = b + r
            continue
        
        elif i > 2:
            b = 'M'*h
            r = b + r
            
    return r

print(roman(100010))
