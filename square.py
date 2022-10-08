a=int(input("Enter a number :-"))
b=input("what do You want:-\n 'square' 'cube' 'power':- ")
if (b=="square"):
    sq = a*a
    print("Square of the given number is:- ",sq)
elif (b=="cube"):
    cube= a*a*a
    print("Cube of the given numbers:- ",cube)
elif (b=="power"):
    po=int(input("How many times :-"))
    pow=a**po
    print("Power of the number is :-",pow)