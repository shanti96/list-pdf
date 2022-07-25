a=[1234, 122, 1984, 19372, 100]
b=str(a[0]) 
d=[]
for i in range(0,len(a)): 
    c=str(a[i]) 
    d.append(c)
    print(d)
    if b[0]==c[0]: 
        if i==len(a)-1: 
            pass
            #print("True") 
    else:
        #print("False") 
        break 

#['aabc', 'abc', 'ab', 'a']    
#