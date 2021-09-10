a=int(input())
ans=[]
for i in range(a):
    odd=0
    even=0
    b=input()
    li=[int(i) for i in input().split(" ")]
    for i in li:
        if i%2==0:
            even+=1
        else:
            odd+=1
    if odd>even:
        for i in range(len(li)):
            if li[i]%2==0:
                ans.append(i+1)
    else:
        for i in range(len(li)):
            if li[i]%2!=0:
                ans.append(i+1)
for i in ans:
    print(i)