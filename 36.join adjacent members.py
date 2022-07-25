a=['1', '2', '3', '4', '5', '6', '7', '8','9']
b=[]
i=0
while i<len(a):
    j=i+1
    while j<len(a):
        b.append(a[i]+a[j])
        j=j+len(a)
    i=i+2  
print(b)      