a=int(input())
s=0
if a>0:
    for i in range(1,a+1):
        if (a%i==0):
            s=s+1
if s==2:
    print(a,"is Prime No.")
else:
    print(a,"is not prime No.")