a=input()
b=int(input())
li=[]
count=0
st=''
for i in range(len(a)):
    st+=a[i]
    count+=1
    if count%b==0:
        count=0
        li.append(st)
        st=''
if st!='':
    li.append(st)
li=[int(i) for i in li]
ans=[]
for i in li:
    if i in [2,3,5,7]:
        ans.append(i)
    elif i%2==0 or i%3==0 or i%5==0 or i%7==0 or i==1:
        continue
    else:
        ans.append(i)
if len(ans)>0:
    for i in ans:
        print(i)
else:
    print('NA')

    
