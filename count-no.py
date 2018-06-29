'''num=int(input('enter the no:'))
d=int(input('enter the digit to count:'))
c=0
while(num!=0):
    r=num%10
    num=num//10
    if(d==r):
        c=c+1
print(d,"exist",c,"times in number")'''

num=int(input('enter the no:'))
sum=0
while(num!=0):
    r=num%10
    sum=sum+r
    num=num//10
print(sum,"sum of digits")