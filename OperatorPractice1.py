s=input()
l=len(s)
s=list(s)
if l==5:
    temp=s[-1]
    s[-1]=s[0]
    s[0]=temp
    s1=""
    for i in s:
        s1+=i
    print(s1)