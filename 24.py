f=open('24.txt')
s=f.readline()
mxl=1
ans=1
for i in range(1, len(s)-1):
    if s[i] in 'AC' and (s[i]==s[i+1] or s[i]==s[i-1]):
        ans+=1
    else:
        mxl=max(mxl, ans)
        ans=0
mxl=mxl//2 # т. к. считаем кол-во пар
print(mxl)