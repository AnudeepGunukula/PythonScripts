a=int(input())
st=str(bin(a))
st=st.replace("0b","")
c=len(st)-st.index('1')-1
st=st[::-1]
b=st.index('1')
a=st.count('1')
print(f"{a}#{b}#{c}")

