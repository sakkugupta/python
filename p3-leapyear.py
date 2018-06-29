'''year=int(input('enter your year:'))
if(year%4==0):
    print(year,'is leap year')
else:
    print(year,'is not leap year')'''

year=int(input('enter your year:'))
if(year%100==0):
    if(year%400==0):
        print(year,'is leap')
    else:
        print(year,'is not leap')
else:
    if(year%4==0):
        print(year,'is leap year')
    else:
        print(year,'is not leap')