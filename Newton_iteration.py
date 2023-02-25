def f(x):
    return (x - 3) ** 3

def df(x):
    return 3 * ((x - 3) ** 2)

def newtonMethod(n, assume):
    time = n
    x = assume
    Next = 0
    A = f(x)
    B = df(x)
    print(f"A = {A}, B = {B}, time = {time}")
    if f(x) == 0.0:
        return time, x
    else:
        Next = x - A/B
        print(f"Next = {Next}")
    if abs(A - f(Next)) < 1e-6:
        print(f"Meet f(x) = 0, x = {Next}")
    else:
        return newtonMethod(n + 1, Next)

print(newtonMethod(0, 4))

def sef_newton(x):
    A = f(x)
    B = df(x)
    Next = 0
    if (A == 0):
        return x
    else:
        Next = x - A/B
        if(abs(A - f(Next)) < 1e-6):
            return x
        else:
            return sef_newton(Next)
print(sef_newton(4))