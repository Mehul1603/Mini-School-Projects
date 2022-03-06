a=[95,79,19,43,52,2]
l = len(a)

#Choose one sorting technique by removing their docstrings

#Bubble Sort

for i in range(l):
    for j in range(l-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]


#Reverse Bubble Sort (but better)
'''
for i in range(1,l):
    k = i
    for j in range(0,i):
        if a[k]<a[i-1-j]:
            a[k],a[i-j-1]=a[i-j-1],a[k]
            k = i-j-1
'''

#Another Sort
'''
for i in range(1,l):
    k = a[i]
    j = i-1
    while j>=0:
        if a[j]>k:
            a[j],a[j+1]=a[j+1],a[j]
            j -= 1
        else:
            break
'''

#Selection Sort
'''
for i in range(1,l):
    j = i-1
    k = i
    while a[k]<a[j] and j >= 0:
        a[k],a[j]=a[j],a[k]
        k = j
        j -= 1
'''        

print(a)