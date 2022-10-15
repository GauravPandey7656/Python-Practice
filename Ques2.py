name= input("What is your Name:-")
sal=int(input("What is the Your Salary:-"))
yrs=int(input("How many years spent in company:-"))
if (yrs>=10):
    bonus=(10*sal)/100
    netsal=bonus+sal
    print("Congrats",name," you have got 10 Percent bonus your net salary is :-",netsal)
elif (yrs>=6 and yrs<10):
    bonus=(8*sal)/100
    netsal=bonus+sal
    print("Congrats",name," you have got 8 Percent bonus your net salary is :-",netsal)
elif (yrs<6):
    bonus=(5*sal)/100
    netsal=bonus+sal
    print("Congrats",name,"you have got 5 Percent bonus your net salary is :-",netsal)
else:
    print("invalid input")