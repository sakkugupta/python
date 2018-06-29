'''for i in range(1,6):
    for j in range(1,i):
        print(" ",end="")
    for j in range(1,i+1):
        print("0*",end="")
    for j in range(1,6-i):
        print("  ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(4,0,-1):
    for j in range(1,i):
        print(" ",end="")
    for j in range(i,i+1):
        print("*",end="")
    for j in range(1,6-i):
        print("  ",end="")
    for j in range(1,6-i):
        print("*",end="")
    print()


a='hello'
b=' sakku'
print(a+b)
print(b*2)


count=0
for letter in 'hello':
    if(letter=='l'):
        count+=1
print(count,'letter found')

endswith(): used to check wheather a string is terminated with any particular suffix or not

str='hello.'
print(str.endswith('hello.'))
print(str.endswith('hello'))

isdigit();return ture is string has only  digits otherwise false
isalpha():return true is string has only alphabets otherwise false

str='1234'
print(str.isdigit())
str='1230#$'
print(str.isdigit())
str='hellosakshi'
print(str.isalpha())

len():return length of string

str="hello"
print("length of string is:", len(str))

list=[1,2,3]
print(list)
print(type(list[1]))
a=[1,'hello',2,'sakku']
print(a[3])
print(a[1:4])

a=[1,2,3,4]
b=['a','b']
c=a+b
print(c)
a[2]=4
print(a)
a.append('s')
print(a)
a=['a','b']
b=['c','d']
x=[a,b]
print(x)

#cmp():used to compare two list deprecated inpython 3'''
