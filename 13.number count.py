a=[1, 1, 2, 3, 4, 4, 5, 1]
b=[]
i=0
while i<len(a):
    c=0
    p=a[i]
    while (i<len(a) and p==a[i]):
        c=c+1
        i=i+1
    if (c>1):
        b.append([c,p])
    else:
        b.append(p)
print(b)                