for i in range(5,0,-1):
    for j in range(5,0,-1):
        print("%3d"%j,end="")
    print()


for i in range(6,0,-1):
    for j in range(1,7):
        print(i,end="\t")
    print()

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="\t")
    print()

for i in range(1,6):
    for j in range(i,i+5):
        print(j,end="\t")
    print()

for i in range(9,4,-1):
    for j in range(i,i-5,-1):
        print(j,end="\t")
    print()

for i in range(6,0,-1):
    for j in range(1,7):
        print(chr(i+64),end='\t')
    print()

for i in range(1,6):
    for j in range(i,i+5):
        print(chr(i+64),end="\t")
    print()

for i in range(1,10):
    a=1
    for j in range(1,10):
        if(j%2==0):
            print(a,end="\t")
            a=a+1
        else:
            print("*",end="\t")
    print()

for i in range(1,10):
    for j in range(1,8):
        print(j%2,end="\t")
    print()

k=1
for i in range(1,8):
    for j in range(1,8):
        if(k==1):
            print(k,end="\t")
            k=0
        else:
            print(k,end="\t")
            k=1
    print()


