pocket_number = int(intput("enter a pocket number"))
if(pocket_number==0):
    print("green")
elif(pocket_number<=10):
    if(pocket_number%2==0):
        print("black")
    else:
        print("red")
elif(pocket_number<=18):
    if(pocket_number%2==0):
        print("red")
    else:
        print("black")
elif(pocket_number<=28):
    if(pocket_number%2==0):
        print("black")
    else:
        print("red")
elif(pocket_number<=36):
    if(pocket_number%2==0):
        print("red")
    else:
        print("black")
else:
    print("error")
