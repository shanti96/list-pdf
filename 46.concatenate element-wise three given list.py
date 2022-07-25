a=['0', '1', '2', '3', '4']
b=['red', 'green', 'black', 'blue', 'white']
c=['100', '200', '300', '400', '500']
add=[]
for i in range(0,len(a)):
    p=a[i]+b[i]+c[i]
    add.append(p)
print(add)

#['0red100', '1green200', '2black300', '3blue400', '4white500']