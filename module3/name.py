def patternprint(name):
    matrix = [[' ' for i in range(0,4)] for j in range(0,4)]
    if(name=='a'):
        for i in range(0,4):
            for j in range(0,4):
                if(i==0 or i==1):
                    matrix[i][j] = '*'
                elif(j==0 or j==3):
                    matrix[i][j] = '*'
    elif(name=='k'):
        for i in range(0,4):
            for j in range(0,4):
                if((j==0 or (j==i+i)) and i!=0):
                    matrix[i][j] = '*'
                elif(j==i-1 and i>=2):
                    matrix[i][j] = '*'
                elif(i==0 and (j==0 or j==3)):
                    matrix[i][j] = '*'
    elif(name=='h'):
        for i in range(0,4):
            for j in range(0,4):
                if(j==0 or i==2 or j==3):
                    matrix[i][j] = '*'
    elif(name=='r'):
        for i in range(0,4):
            for j in range(0,4):
                if((i==0 or i==1)):
                    matrix[i][j] = '*'
                elif(j==i-1 or j==0):
                    matrix[i][j] = '*'
    elif(name=='p'):
        for i in range(0, 4):
            for j in range(0,4):
                if(j==0):
                    matrix[i][j] = '*'
                if(i==0 or i==1):
                    matrix[i][j] = '*'
    return matrix
name = "prakhar"
for i in name:
    matrix = patternprint(i)
    for i in range(0,4):
        for j in range(0,4):
            print(matrix[i][j], end='')
        print("",end='\n')
    print(" ",end='\n')
