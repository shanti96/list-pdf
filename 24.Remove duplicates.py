lis= [1,2,3,1,2,2]
a=[]
for i in range(0,len(lis)):
    if lis[i] not in a:
        a.append(lis[i])
print(a)        