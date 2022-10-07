print("Hello, Today we will find The Area of Triangle")
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