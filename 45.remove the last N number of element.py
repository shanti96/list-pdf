a=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
remove=int(input("enter the last number remove"))
b=[]
for i in range(0,len(a)-remove):
    b.append(a[i])
print(b)    