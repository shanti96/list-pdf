a=[1, 1, 2, 3, 4, 5, 1, 2]
b=[]
for i in range(0,len(a)):
    if a[i]>1:
        b.append(a[i])
print(b)      

##
n=[5, 6, 7, 8, 9, 10]
k=[]
for i in range(0,len(n)):
    p=n[i]
    if p not in k :
        k.append(p)
k.remove(7)
print(k)    