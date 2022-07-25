a=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
b=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
c=[] 
for i in range(0,len(a)):
    for j in range(0,1):
        c.append(a[i]+b[i])
print(c)        