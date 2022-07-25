a=[5, 6, [], 3, [], [], 9]
b=[]
for i in range(0,len(a)):
    p=a[i] 
    if p not in b:
        b.append(p)
b.remove([])
print(b)                      