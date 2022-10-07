a = input("Enter what you find :-\n for eg. Triangle, Rectangle, Square and etc.")
if (a=="Triangle"):
    s1=int(input("Enter side A:-"))
    s2=int(input("Enter side B:-"))
    s3=int(input("Enter side C:-"))
    Sm=s1+s2+s3
    S=Sm/2
    sa=S-s1
    sb=S-s2
    sc=S-s3
    ml=(S*sa*sb*sc)
    ud=ml**0.5
    print("Area of the Triangle is :-", ud)
elif (a=="Rectangle"):
    l=int(input("Enter the Lenght of rectangle:-"))
    b=int(input("Enter the Bredth of rectangle:-"))
    a=l*b
    print("Area of the Rectangle is :-", a)
elif (a=="Square"):
    a=int(input("Enter the side of square :-"))
    sq=a**2
    print("Area of the Square is :-", sq)
print("ThankYou for Using our Services. :) \n I thing Your query is Solve.\n Be Happy Always Smile")