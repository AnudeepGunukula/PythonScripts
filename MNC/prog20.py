fu=[int(i) for i in input().split(" ")]
ck=[int(i) for i in input().split(" ")]
maxi=0
count=0
for i in range(len(fu)):
    if ck[i]-fu[i]>=0:
        count+=ck[i]-fu[i]
        if count>maxi:
            maxi=count
    else:
        count=0
print(maxi)