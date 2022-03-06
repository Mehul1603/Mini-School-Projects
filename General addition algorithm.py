import math

def mult(a,b):
    s = math.fabs(b)/b
    
    if b != s*1:
        return s*a + mult(a, b - s*1)

    else:
        return s*a
    
print(mult(-2,-3))
