a=[1, 2, 3, 4, 5, 6] 
c=[]
for i in range(0,len(a)):
    b=[]
    p=a[i] 
    b.append(p)
    for j in range(i+1,len(a),len(a)):
        b.append(a[j])
        c.append(b)
print(c)        