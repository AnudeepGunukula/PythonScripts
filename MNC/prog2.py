st=[i for i in input()]
finalans=[]
for i in range(len(st)):
    li=[]
    for j in range(i,len(st)):
        if st[j] in li:
            ans=len(st[i:j])
            finalans.append(ans)
            break
        else:
            li.append(st[j])

if len(finalans)==0 :
    print(len(st))
else:
    print(max(finalans))


