i=1
n=int(input("enter the number"))
p=n
while i<n:
    j=1
    while j<i:
        print(" ",end="")
        j=j+1
    a=65
    k=1
    while k<=p:
        print(chr(a),end="")
        k=k+1
        a=a+1
    i=i+1
    print()
    p=p-2

