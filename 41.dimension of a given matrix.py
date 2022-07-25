a=[[0, 1, 2], [2, 4, 5]]
for i in range(0,len(a)):
    b=[]
    element=0
    for j in range(0,len(a[i])):
        element=element+1
    b.append(len(a))
    b.append(element)
print(b)    