#a=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
a=[[1], [2, 4, 4], [1, 2], [4]] 
b=[]
i=0
c=0
for k in range(0,len(a)):
    if c<=len(a[k]):
        c=len(a[k])
while i<len(a): 
    if i<c:
     sum=0
     s=0
     j=0
     while j<len(a): 
        if len(a[j])>i:
           sum=sum+a[j][i]
           s=s+1 
        j=j+1 
     average=sum/s 
     b.append(average) 
    i=i+1 
print(b)    

#[4.8, 5.8, 6.8, 8.0, 11.0]
#[8, 6, 4]