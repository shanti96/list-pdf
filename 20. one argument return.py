a=[20,37,20,21]
b=[]
for i in range(0,len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)        

###
n=[1,1,1,1] 
ap=[]
i=0
while i<len(n):
    a=n[i]
    count=0
    j=i
    while j<len(n):
        p=n[j]
        j=j+1
        if count<=2 and a==p:
            count=count+1
            if count==2:
                ap.append(a)
                i=i+1    
    i=i+1
print(ap)        