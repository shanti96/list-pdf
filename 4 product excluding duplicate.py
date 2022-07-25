#List product excluding duplicates.
list1 = [6,1,3,5,6,3,1]
a=1
i=0
while i<len(list1):
    n=list1[i]
    s=0
    j=0
    while j<=i:
        p=list1[j]
        j=j+1
        if n==p:
           s=s+1
    if s==1:
        a=a*n
    i=i+1
print(a)               