l=["Red","black","Blue","Red"]
Cars=["NANO","TATA","ALTO","JEEP"]
num=[1,4,6,2,10]

newlist=[x.lower() for x in Cars if x!="NANO"]
print(newlist)
num.sort(reverse=True)
print(num)


# for x in range(len(l)):
#     print(l[x])
# while x<len(l):
#     print(l[x])
#     x+=1
# [print(x) for x in Cars]
# for i in Cars:
#     if "A" in i:
#         newlist.append(i)