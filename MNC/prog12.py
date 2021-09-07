l=[int(i) for i in input().split()]
a,b=l[0],l[1]

biglist=[]
for i in range(b):
    flag=0
    z=[int(i) for i in input().split()]
    x,y=z[0],z[1]
    if i==0:
        biglist.append([x,y])
    else:
        for i in biglist:
            if x in i:
                i.append(y)
                flag=1
                continue
            if y in i:
                i.append(x)
                flag=1
        if flag==0:
            biglist.append([x,y])
min=len(biglist[0])
for i in biglist:
    if len(i) < min:
        min=len(i)
        
print(min)
