for A in range(1, 1000):
    p=range(5, 55)
    q=range(50, 94)
    k=0
    for x in range(1, 1000):
        f=(x not in p and x in q) <= (x>A)
        if f==0:
            k+=1
    if k==20:
        print(A)
        break
