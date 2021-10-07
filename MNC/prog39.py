


def getbuilding(input1,input2):
    row=[]
    col=[]
    for i in input2:
        row.append(i[0])
        col.append(i[1])
    row=list(set(row))
    col=list(set(col))
    ans=0
    for i in row:
        ans+=8
    for j in col:
        ans+=8
    ans-=input1
    return ans






a=2
b=[[5,3],[5,5]]
print(getbuilding(a,b))
