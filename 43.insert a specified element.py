a=['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
b=[]
c=3
for i in range(0,len(a)):
    if i ==c:
        b.append('Z')
        c=c+3
    b.append(a[i])
print(b)    

#['s', 'd', 'f', 'Z', 'j', 's', 'a', 'Z', 'j', 'd', 'f', 'Z', 'd']