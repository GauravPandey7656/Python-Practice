P=int(input())
T=int(input())
R=float(input())
a=(1+R/100)**T
A=a*P
CI=A-P
print("{:.2f}".format(CI))