def removeProduct(num,ids,rem):
  arr=ids 
  n=num
  mi=rem
  m = {}
  v = []
  count = 0
 
  for i in range(n):
    if arr[i] in m:
      m[arr[i]] += 1
    else:
      m[arr[i]] = 1
 
  for i in m:
    v.append([m[i],i])
 
  v.sort()
  size = len(v)
  
  for i in range(size):
    if (v[i][0] <= mi):
      mi -= v[i][0]
      count += 1
    else:
      return size - count
  return size - count
      
num=int(input())
ids=input().split(" ")
rem=int(input())
print(removeProduct(num,ids,rem))




