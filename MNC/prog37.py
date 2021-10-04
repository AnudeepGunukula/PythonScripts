

def palprime(L,R):
    x=[2,3,5,7]
    count=0
    for i in range(L,R+1):
         if (i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i!=1) or (i in x):
                if str(i)==str(i)[::-1]:
                      count+=1
    return count




a=int(input())
for i in range(a):
    l,r=map(int,input().split())
    out=palprime(l,r)
    print(out)
