import math

def f(x):
    return x*math.exp(x)*math.cos(x/2)

a=-math.pi
b=math.pi
n=1000
h=(b-a)/n

xx=[]
yy=[]

for i in range(n):
    x=a+i*h
    xx.append(x)
    yy.append(f(x))

c=yy[0]+yy[n-1]
s=0
for i in range(1,n-1):
    s+=2*yy[i]

s1=(h/2)*(c+s)
print("Integral: ",s1)