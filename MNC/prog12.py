m,n=input().split()
biglist=[]
for i in range(int(n)):
    a,b=input().split()
    if i == 0:
        biglist.append([a, b])
        continue
    flag=0
    for x in biglist:
        if a in x:
            x.append(b)
            flag=1
    if flag==0:
        biglist.append([a, b])
ans=100000000
for i in biglist:
    if len(i)<ans:
        ans=len(i)
print(ans)







