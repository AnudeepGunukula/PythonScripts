a=int(input())
li=[int(i) for i in input().split()]
odd,even=[],[]
for i in li:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
ans=[]
odd.sort()
even.sort()
flag=0
for i in range(len(li)):
    if odd[0] < even[0]:
        ans.append(odd[0])
        odd=odd[1:]
        if len(odd)==0:
            for i in even:
                ans.append(i)
            flag=1
    else:
        ans.append(even[0])
        even=even[1:]
        if len(even)==0:
            for i in odd:
                ans.append(i)
            flag=1
    if flag==1:
        break
print(ans)
