num=[1,2,3,4,5]
sqr=[x*x for x in num]
# print(sqr)
num1=[1,2,3,4,5,2,6]
# for i in num:
#     if i==2:
#         a=num.index(2)
#         num[a]=200
#         break
# print(num)
# print(num[::-1])
# num2=num.copy()
num2 = list(num1)
num3 = num1 + num2 + sqr
print(num3)
