li=[int(i) for i in input().split()]

li.sort()

maxi=li[-1]
ans=0

for i in li:
    if i!=maxi:
         ans+=i
    if ans==maxi:
       print(maxi)
       break
