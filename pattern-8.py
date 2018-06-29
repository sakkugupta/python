'''for i in range(1,7):
    for j in range(i,i*2):
        print(i,end="\t")
    print()

for i in range(1,7):
    for j in range(i,0,-1):
        print(j,end="\t")
    print()

for i in range(1,6):
    for i in range(i-1,-1,-1):
        print(2**i,end="\t")
    print()

for i in range(1,6):
    for i in range(0,i):
        print(2**i,end="\t")
    for i in range(i-1,-1,-1):
        print(2**i,end="\t")
    print()

for i in range(1,6):     //error
    n=34-(5*(i-1))+1
    print("  ")*n
    for i in range(0,i):
        print(2**i,end="\t")
    for i in range(i-1,-1,-1):
        print(2**i,end="\t")
    print()'''

print('enter a no:')
number=int(input())
temp=int(number)
sum=0
while(temp!=0):
    rem=temp%10
    sum=sum+(rem*3)
    temp=temp/10
if(number==sum):
    print('armstrong no')
else:
    print('not armstrong no')