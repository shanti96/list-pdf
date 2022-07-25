list1 = [-12, 14, 95, 3]
pos=0
neg=0
for i in range(0,len(list1)):
    p=list1[i]
    if p>0:
        pos=pos+1
    else:
        neg=neg+1
print("positive number=",pos)
print("negtive number=",neg)            