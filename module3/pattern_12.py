#left arrow star pattern
k = 5
for i in range(0,9):
        if(i<5):
            print("*"*(5-i),end='')
        if(i==5):
            print("*"*2,end='')
        if(i>5):
            print("*"*(abs(5-i)+2), end='')
        print("",end='\n')

#plus pattern
for i in range(0, 9):
    for j in range(0,9):
        if(i==4):
            print("*",end='')
        elif(j==4):
            print("*",end='')
        else:
            print("",end=' ')
    print("",end='\n')
print("",end='\n')

#diamond star pattern
for i in range(0, 7):
    for j in range(0, 7):
        if(i<=3):
            if(j>=3-i and j<=3+i):
                print("*",end='')
            else:
                print(" ",end='')
        else:
            if(j>i-4 and j<7-(i-3)):
                print("*",end='')
            else:
                print(" ",end='')
    print("",end='\n')
print("",end='\n')

#hollow pyramid
k=0
for i in range(0, 9):
    for j in range(0, 17):
        if(j==8-k or j==8+k or i==8):
            print("*",end='')
        else:
            print(" ",end='')
    print("",end='\n')
    k+=1
print("",end='\n')
