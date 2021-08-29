a= int(input())
b=[int(i) for i in input().split()]
max=-999999999
summ=0
for i in b:
    summ+=i
    if summ > max:
        max=summ
    if summ<0:
        summ=0
print(max)


