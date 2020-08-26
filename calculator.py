
def add(x,y):
    return x+y
def factorial(n):
    x=1
    for i in range(1,n+1):
        x*=i
    return x
def sin(x,N):
    s=0
    for n in range(N+1):
        s+=(((-1)**n)*x**(2*n+1))/(factorial(2*n+1))
    return s
def divide(x,y):
    return x/y
def root(number,rootnr=2):
    return number**(1/rootnr)
def absolute(x):
    if x<0:
        return -x
    return x