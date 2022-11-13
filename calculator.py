def add(a,b):
    sum=a+b
    print("sum of the no. is :",sum)
def sub(a,b):
    sub=a-b
    print("Subtract of the no. is :",sub)
def div(a,b):
    div=a/b
    print("Divison of the no. is :",div)
def mul(a,b):
    mul=a*b
    print("Multiplication of the no. is :",mul)
p=int(input("Enter no. a :"))
q=int(input("Enter no. b :"))
s=input("add,sub,mul,div :")
if "add" in s:
    add(p,q)
elif "sub" in s:
    sub(p,q)
elif "mul" in s:
    mul(p,q)
elif "div" in s:
    div(p,q)
