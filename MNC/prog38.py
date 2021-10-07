
a=int(input())
b=[int(i) for i in input().split()]


c=sorted(b)[::-1]
i=0
ans=0
while True:
    x=a-b.index(c[i])
    if x>=0:
        a=x
        ans+=c[i]
        if a==0:
            break
        i=0
    i+=1
print(ans)
