def find_common(n,a,m,b,s,c):
    asize,bsize,csize=len(a),len(b),len(c)
    li=[len(a),len(b),len(c)]
    li.sort()
    ans=[]
    if li[0]==asize:
        checklist=a
    elif li[0]==bsize:
        checklist=b
    else:
        checklist=c
    for i in checklist:
            if i in a:
                if i in b:
                    if i in c:
                        ans.append(i)
    mini=100000000000000
    for i in ans:
        if i<mini:
            mini=i
    return mini
        
