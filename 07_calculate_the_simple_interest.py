# Question: Write a Python program to calculate the simple interest using a function.

p = 10000
r = 12
t = 4

def calculate_simple_interest(p,r,t):
    si = (p*r*t)/100
    return si

print(calculate_simple_interest(p,r,t))