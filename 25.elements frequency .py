lis =[4, 6, 4, 3, 3, 4, 3, 4,]
a=[]
i=0
while i<len(lis):
    n=lis[i]
    j=0
    count=0
    while j<len(lis):
        p=lis[j]
        j=j+1
        if p==n:
          count=count+1 
    if count>=2 and n not in a:
        a.append(n)
    i=i+1
print(a)                 