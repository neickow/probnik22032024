def f(n, f):
    s = 0
    while n > 0:
        s += n % f
        n = n // f
    return s == 75
for n in range(2, 100):
    s=n ** 25 - 2 * n ** 13 + 10
    if f(s, n):
        print(n)
        break
