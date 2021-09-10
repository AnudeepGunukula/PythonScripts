def decimalToBinary(n):
    return "{0:b}".format(int(n))
li=input().split(" ")
glob=0
for i in range(1,int(li[0])+1):
        count=0
        b=decimalToBinary(i)
        for i in range(len(b)):
            if b[i:i+3]=='101':
                count+=1
        if(count>=int(li[1])):
            glob+=1
print(glob)
    