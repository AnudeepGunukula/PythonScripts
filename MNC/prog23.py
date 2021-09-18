li =input().split()
fu=li.copy()
li.sort()
for i in range(len(li)-1): 
    if li[i][0]==li[i+1][0]:
        if fu.index(li[i]) > fu.index(li[i+1]):
               temp=li[i]
               li[i]=li[i+1]
               li[i+1]=temp             
print(" ".join(li))
