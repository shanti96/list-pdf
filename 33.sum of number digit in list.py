a=[15, 81, 11, 234]
b=[]
i=0
while i <len(a):
    j=0
    p=str(a[i])
    sum=0
    while j<len(p):
        s=int(p[j])
        sum=sum+s
        j=j+1
    b.append(sum) 
    i=i+1
print(b)       