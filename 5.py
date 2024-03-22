def f(a, b, n):
    if a==b:
        return n
    if a>b:
        return False
    return f(a+8, b, n+'1') or f(a*2, b, n+'2')
print(f(45, 376, ''))