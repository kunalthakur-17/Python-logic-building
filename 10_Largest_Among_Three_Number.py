# Largest Among Three Numbers 

a = -10
b= -2
c = -4

def Largest_Among_Three_Numbers(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(Largest_Among_Three_Numbers(a, b, c))