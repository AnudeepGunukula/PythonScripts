a=int(input())
li=[int(i) for i in input().split()]
ans=0
for i in range(len(li)-1):
    ans+=abs(li[i]-li[i+1])
print(ans)
