a=[2, 4, 6, 8]
i=0
j=1
b=[]
while i<len(a):
    p=a[i]
    s=0
    if j<len(a):
        k=a[j]
        while p<k:
           p=p+1
           s=s+1
        b.append(s) 
    i=i+1  
    j=j+1   
print(b)         