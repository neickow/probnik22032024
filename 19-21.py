from math import ceil
print('19 ЗАДАНИЕ')
def f(a, p):
    if a==1 and p==6:
        return True
    if a==1 and p!=6:
        return False
    if p%2==1:
        return any(f(i, p+1) for i in range(ceil(a/2), a))
    if p%2!=1:
        return all(f(i , p+1) for i in range(ceil(a/2) , a))
ans=0
for i in range(100, 2, -1):
    if f(i, 1):
        print(i)
        break
print('20 ЗАДАНИЕ')
from math import ceil
def f(a, p):
    if a==1 and p==5:
        return True
    if a==1 and p!=5:
        return False
    if p%2==0:
        return all(f(i, p+1) for i in range(ceil(a/2), a))
    if p%2!=0:
        return any(f(i , p+1) for i in range(ceil(a/2) , a))
ans=0
for i in range(2, 100):
    if f(i, 1):
        ans+=1
print(ans)
print('21 ЗАДАНИЕ')
from math import ceil
from functools import lru_cache
@lru_cache(None)
def f(a, p):
    if a==1 and p==5:
        return True
    if a==1 and p!=5:
        return False
    if p%2==0:
        return any(f(i, p+1) for i in range(ceil(a/2), a))
    if p%2!=0:
        return all(f(i , p+1) for i in range(ceil(a/2) , a))
ans=0
for i in range(100, 1000):
    if f(i, 1):
        ans+=1
print(ans)


