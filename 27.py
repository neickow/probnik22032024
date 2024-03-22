f=open('27-A.txt')
s=[int(x) for x in f.readlines()]
N=s.pop(0)
ans=0
for i in range(N-1):
    for j in range(i+1, N):
        if (s[i]+s[j])%2==0 and s[i]>0 and s[j]>0:
            for n in range(i+1, j):
                if s[n]==0:
                    ans+=1
                    break
print(ans)