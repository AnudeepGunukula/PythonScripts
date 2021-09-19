a=int(input())
if a==0:
    return 0
i=0
count=0
li=[1,2,3]
while(i<a):
    i+=li[count]
    count+=1
    if count%3==0:
        count=0
if i==a:
    return 1
else:
    return 0
