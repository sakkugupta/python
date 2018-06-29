dict={'fname':'sakshi'+'gupta','secondname':'sakku','dob':'10/08/96'}
print(dict)
#print(dict['frame']) //not working

#updation

dict['fname']='sakku'
print(dict)
dict['age']='12'
print(dict)

#empty dictionary
dict.clear()
print(dict)

#nested dictonary
dict={'fname':'sakshi','more':{'first':'sak','second':'shi'},'age':16}
print(dict)
print(dict['more']['second'])
print(dict['more'])

#copy dictionary
sak=dict.copy()
print(sak)

print(dict.keys())

#dictionary from keys
a=[1,2,3]
x=dict.fromkeys(a,10)
print(x)
dict={'a':[10,20],'b':'hey'}
dict1=dict['b']
print(dict1)


#update dictionary
dict1.update(dict1)
print(dict1)


#not working
word='hey'
d=dict()
for e in word:
    if e not in d:
        d[e]=1
    else:
        d[e]=d[e]+1
print(d)
d.delitem('h')
print(d)
#delete item
d.pop('e')
print(d)
#till this
