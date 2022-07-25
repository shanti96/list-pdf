a=['Red', 'Maroon', 'Yellow', 'Olive']
c=[]
for i in range(0,len(a)):
    b=[]
    for j in range(0,len(a[i])):
        b.append(a[i][j])
    c.append(b)
print(c)   

#[['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]