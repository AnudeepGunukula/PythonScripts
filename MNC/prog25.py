li=input1
li.sort()
x=0
ans=[]
while(x<len(li)-1):
    if li[x]==li[x+1]:
        ans.append(li[x])
        x+=1
    if (li[x]+1)!=li[x+1]:
        ans.append(li[x]+1)
    x+=1
return ans
