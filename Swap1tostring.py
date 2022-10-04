a=input()
b=list(a)
c=b[0]
d=int(c)
if (d%2==0):
    print(a)
else:
    b[0]="o"
    for i in b:
        print(i, end="")