fu=[int(i) for i in input().split(" ")]
ck=[int(i) for i in input().split(" ")]
it=[]
for i in range(len(fu)):
    it.append([fu[i],ck[i]])
points=int(input())
it.sort()
it=it[::-1]
ans=0
for i in it:
    if points-i[1]>=0:
      points-=i[1]
      ans+=i[0]
print(ans)