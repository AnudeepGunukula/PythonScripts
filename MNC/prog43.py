def palindrome(st):
    if st.lower()==st[::-1].lower():
        return True
    return False

n=int(input())
li=[]
ans=[]
for i in range(n):
    li.append(input())
for test_str in li:
    res = [test_str[i: j] for i in range(len(test_str)) for j in range(i + 1, len(test_str) + 1)]
    res.sort(key=len)
    res=res[::-1]
    for i in res:
        if palindrome(i):
            ans.append(len(i))
            break
for i in ans:
    print(i)
