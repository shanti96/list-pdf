a=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
n=input("enter any charecter")
if n in a:
    for i in range(0,len(a)):
        if a[i]==n:
            p=i
print(p)       