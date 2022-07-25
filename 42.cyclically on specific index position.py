a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
b=[]
c=int(input("enter number"))
for i in range(c,len(a)):
    b.append(a[i])
for j in range(0,c):
    b.append(a[j])    
print(b)        