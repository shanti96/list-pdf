n=[4, 5, 5, 5, 3, 8]
a=[]
for i in range(0,len(n)):
    p=n[i] 
    count=0
    for j in range(i,len(n)):
        k=n[j]
        if k == p:
            count=count+1
    if count>=3: 
        a.append(p)
print(a)      