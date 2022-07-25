lis=[[2,4],[2,9,3],[1,0,5],[5,8,7,9]]
a=[]
i=0
while i<len(lis):
    p=len(lis[i])
    a.append(p)
    a.append(lis[i])
    i=i+1
print("lengthcount=",a)

i=0
b=[]
while i<len(lis):
    j=0
    s=0
    while j<len(lis[i]):
        p=lis[i][j]
        s=s+p
        j=j+1
    av=s/len(lis[i])
    b.append(av)
    i=i+1
print("average=",b)    