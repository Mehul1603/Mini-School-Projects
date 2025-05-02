#https://www.hackerrank.com/challenges/queens-attack-2/problem

def queensAttack(n, k, r_q, c_q, obstacles):

    nosq = 0
    for i in range(c_q+1,n+1):
        x = [r_q,i]
        if x not in obstacles:
            nosq += 1
        else:
            break
            
    for i in range(c_q-1,0,-1):
        x = [r_q,i]
        if x not in obstacles:
            nosq += 1
        else:
            break
        
    for i in range(r_q+1,n+1):
        x = [i,c_q]
        if x not in obstacles:
            nosq += 1
        else:
            break
        
    for i in range(r_q-1,0,-1):
        x = [i,c_q]
        if x not in obstacles:
            nosq += 1
        else:
            break
        
    i = r_q+1
    j = c_q+1
    while i<=n and i>= 1 and j<=n and j >= 1:
        x = [i,j]
        if x not in obstacles:
            nosq += 1
        else:
            break
        i += 1
        j += 1
        
    i = r_q-1
    j = c_q+1
    while i<=n and i>= 1 and j<=n and j >= 1:
        x = [i,j]
        if x not in obstacles:
            nosq += 1
        else:
            break
        i -= 1
        j += 1
        
    i = r_q+1
    j = c_q-1
    while i<=n and i>= 1 and j<=n and j >= 1:
        x = [i,j]
        if x not in obstacles:
            nosq += 1
        else:
            break
        i += 1
        j -= 1
        
    i = r_q-1
    j = c_q-1
    while i<=n and i>= 1 and j<=n and j >= 1:
        x = [i,j]
        if x not in obstacles:
            nosq += 1
        else:
            break
        i -= 1
        j -= 1

    return nosq


def queensAttack2(n, k, r_q, c_q, obstacles):
    nosq = 0
    
    sc = []     #same column c_q > obs
    sr = []     #same row r_q > obs
    scp = []    #same column c_q < obs
    srp = []    #same row r_q < obs
    
    tr = []
    utr = n - min(r_q,c_q)
    tl = []
    utl = min(r_q-1,n-c_q)
    br = []
    ubr = min(c_q-1,n-r_q)
    bl = []
    ubl = min(r_q,c_q) - 1
    
    for i in obstacles:
        if i[0] == r_q:
            if i[1]-c_q>0:
                srp += [i[1]-c_q]
            else:
                sr += [c_q-i[1]]
            
        elif i[1] == c_q:
            if i[0]-r_q>0:
                scp += [i[0]-r_q]
            else:
                sc += [r_q - i[0]]
                
        else:
            if not tr:
                for a in range(1,utr+1):
                    x = [r_q+a,c_q+a]
                    if x == i:
                        tr = a
                        break
            if not tl:    
                for a in range(1,utl+1):
                    x = [r_q-a,c_q+a]
                    if x == i:
                        tl = a
                        break
            if not br:
                for a in range(1,ubr+1):
                    x = [r_q+a,c_q-a]
                    if x == i:
                        br = a
                        break
            if not bl:        
                for a in range(1,ubl+1):
                    x = [r_q-a,c_q-a]
                    if x == i:
                        bl = a
                        break
            
    if sc:
        nosq += min(sc)-1
    else:
        nosq += c_q-1
    if sr:
        nosq += min(sr)-1
    else:
        nosq += r_q-1
    if scp:
        nosq += min(scp)-1
    else:
        nosq += n-c_q
    if srp:
        nosq += min(srp)-1
    else:
        nosq += n-r_q
    if tr:
        nosq += min(tr)-1
    else:
        nosq += utr
    if tl:
        nosq += min(tl)-1
    else:
        nosq += utl
    if br:
        nosq += min(br)-1
    else:
        nosq += ubr
    if bl:
        nosq += min(bl)-1
    else:
        nosq += ubl
    
    return nosq