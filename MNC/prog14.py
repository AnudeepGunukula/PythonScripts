from itertools import combinations

a=int(input())
ans=[]
for i in range(a):
      count=0
      x=int(input())
      li=list(range(1,x+1))
      for c in range(len(li),0,-1):
          for d in range(c):
              pass
          count+=1
      ans.append(count)
        
for i in ans:
    print(i)