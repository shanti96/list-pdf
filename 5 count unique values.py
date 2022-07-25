#5. Count unique values inside a list.
list1 = [1, 2, 2, 5, 8, 4, 4, 8] 
i=0
k=[]
while i<len(list1):
    n=list1[i]
    p=0
    s=0
    while p<=i:
        a=list1[p]
        p=p+1
        if n==a:
            s=s+1
    if s==1:
        k.append(n)
    i=i+1
print("unique values=",k)        