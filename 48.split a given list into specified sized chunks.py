a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
c=[]
n=int(input("enter the number"))
#for i in range(0,len(a),n):
#    c.append(a[i:i+n])
#print(c)            

i=0
while i<len(a):
    c.append(a[i:i+n])
    i=i+n
print(c) 