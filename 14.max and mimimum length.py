a=[ [1, 3],[0], [5, 7],  [13, 15, 17],[9, 11]]
i=0
m=1
min=1
while i<len(a):
    j=0
    while j<len(a[i]):
        p=len(a[i])
        if p>=m:
            m=p
            max=a[i]
        if p<=min:
            min=p
            minimum=a[i] 
        j=j+1
    i=i+1   
print("maximum length=",m, max) 
print("minimum length=",min, minimum)                  