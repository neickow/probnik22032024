def f(a, k):
    if k == 5:
        return a
    return f'{f(a + 4, k + 1)} {f(a * 2, k + 1)}'
ans=len(set(f(2, 0).split()))
print(ans)