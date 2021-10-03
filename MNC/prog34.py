def alttab(input1,input2,input3):
    x=input3[input2-1]
    input3=input3[:input2-1]+input3[input2:]
    li=[]
    li.append(x)
    return li+input3
     
     
a=int(input())
b=int(input())
c=[int(i) for i in input().split(" ")]
print(alttab(a,b,c))
