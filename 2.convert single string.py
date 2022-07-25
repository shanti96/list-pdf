#2. Convert Character Matrix to single String;
list= [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
i=0
sum=""
while i<len(list):
    n=0
    while n<len(list[i]):
        p=list[i][n]
        sum=sum+p
        n=n+1
    i=i+1    
print(sum) 