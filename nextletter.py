a=input()
if a>= "A"and a<="X" or a>="a" and a<="x":
    a=a.upper()
    a=chr(ord(a)+1)
    b=chr(ord(a)+1)
    print(*a+b,sep=" ")
