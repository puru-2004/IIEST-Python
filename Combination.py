def f(x):
    a=1
    for i in range(x,0,-1):
        a*=i
    return a

print(f(100)/(f(3)*f(97)))