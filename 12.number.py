num=['7','0','3','0','4']
for i in range(0,len(num)):
    a=""
    p=num[i]
    if p>"0":
        a=a+p 
    elif p=="0":
        continue       
    for j in range(i+1,len(num)):
         a=a+"0"
    if i<= len(num)-2:
        a=a+"+"   
    print(a,end="")        