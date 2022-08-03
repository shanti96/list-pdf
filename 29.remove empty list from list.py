a=[5, 6, [], 3, [], [], 9]
b=[]
for i in range(0,len(a)):
    p=a[i] 
    if type(p)==int:
        b.append(p)
print(b)                      