a=int(input())
vow=['a','e','i','o','u']
ans=[]
for i in range(a):
    b=input()
    b=b.lower()
    st=''
    for c in b:
        if c in vow:
            continue
        else:
            st+=c
    st='*'.join(st)
    ans.append(st)
for i in ans:
    print(i)


