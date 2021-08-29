a=int(input())
li=[int(i) for i in input().split()]
flag=0
for i in range(len(li)-1):
    summ=0
    for j in range(i,len(li)):
        summ+=li[j]
        if summ==0:
            flag=1
            break
    if flag==1:
        break
print(flag)

