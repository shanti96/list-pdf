a=[[1], [2, 4, 4], [1, 2], [4]]
#a=[[1, 2, 4], [2, 4, 4], [1, 2]]
b=[] 
c=0
for k in range(0,len(a)):
   if c<=len(a[k]):
      c=len(a[k])
for i in range(0,len(a)): 
   if i<c: 
      sum=0
      for j in range(0,len(a)): 
        if len(a[j])>i:
          p=a[j][i]
          sum=sum+p        
      b.append(sum)  
print(b)  

#[8, 6, 4] 
#[4, 8, 8]