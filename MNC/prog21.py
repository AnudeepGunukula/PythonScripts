def stock_price(a,b):
    A=[]
    for i in range(0,14):
        temp=b[i]-a[i]
        A.append(temp)
    max_so_far=0
    count=0
    for i in A:
        if(i<0):
            count=0
        else:
            count+=i
            if count>max_so_far:
                max_so_far=count
    return max_so_far
    
        
        
