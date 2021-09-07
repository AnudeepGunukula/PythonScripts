a=int(input())
ind=[]
for i in range(a-1):
    ind.append([i,i+1])
b=[i for i in input().split()]
c=[[int(b[i]),int(b[i+1])] for i in range(len(b)-1) if i%2==0]
c=sorted(c,key=lambda x:x[0:2])
slope=[]
for i in ind:
    y=int(c[i[1]][1])-int(c[i[0]][1])
    x=int(c[i[1]][0])-int(c[i[0]][0])
    slope.append(y/x)
l=list(set(slope))
if len(l)==1:
    m=int(l[0])
    c=-m*c[0][0]+(c[0][1])
    print("{m}x-1y={c}".format(m=m,c=c))
else:
    print(0)
