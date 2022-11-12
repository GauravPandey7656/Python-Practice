import sys
print(sys.getrecursionlimit())
def hello():
    print("Hello World ")
    hello()
hello()
