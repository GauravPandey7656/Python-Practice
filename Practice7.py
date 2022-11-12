def fact_recursion(num):
    if num==1:
        return num
    return num*fact_recursion(num-1)
print(fact_recursion(5)) 
