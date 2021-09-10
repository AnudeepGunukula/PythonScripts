from itertools import combinations
a=input()
b=[int(i) for i in input().split(" ")]
c=[int(i) for i in input().split(" ")]
li=[]
flag=0
summ=0
if(c[0]>c[1]):
    print(-1)
else:
    for i in range(len(b),0,-1):
         comb=combinations(b,i)
         for i in comb:
            summ=0
            for j in i:
                summ+=j
            if summ%c[1]==c[0]:
                anslen=len(i)
                flag=1
                break
         if(flag==1):break              
    print(len(b)-anslen)