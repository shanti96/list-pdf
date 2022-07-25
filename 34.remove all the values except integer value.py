a=[34.67, 12, -94.89, 'Python', 0, 'C#']
b=[]
for i in range(0,len(a)):
    p=a[i]
    if type(p)==int:
        b.append(p) 
print(b)         