x=input("Hello World,\n Press Enter to Start finding.")
a = input("Enter what you find :-\n for eg. Area of Triangle, Area of Rectangle, Area of Square and etc.")
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
elif (a!="Triangle","Square","Rectangle"):
    print("Your word enter the wrong way. \n Let's Correct it.\n For example if we finding the Area of Rectangle then Simply write ('Triangle' or 'Rectangle' or 'Square') Let's Try Again \n Please Rerun the Code and not doing any mistake. :)")
print("ThankYou!")