f=open('17.txt')
s=[int(x) for x in f.readlines()]
sr=sum(s)/len(s)
mxs=0
k=0
for i in range(1, len(s)-2):
    if s[i]*s[i+1]>s[i-1]*s[i+2]:
        mxs=max(mxs, s[i]+s[i+1])
        if s[i]>sr or s[i+1]>sr:
            k+=1
print(mxs, k)