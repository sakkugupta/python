'''x=1
for i in range(1,6):
    for j in range(1,4):
        print("%3d"%x,end='\t')
        x=x+1
    print()'''

for i in range(1,5):
    for j in range(1,7):
        if(i%2==0):
            print(j,end="\t")
        else:
            print('*',end="\t")
    print()
