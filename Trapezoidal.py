def Trapezoidal(f, a, b, n):
    h = float(b - a)/n
    s = 0.0
    s += f(a)+f(b)
    for i in range(1, n):
        s += sum([2* f(a + i*h)])
    s *= h/2.0
    return s 
