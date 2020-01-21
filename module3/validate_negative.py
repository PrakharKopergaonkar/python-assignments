noofitems = int(input("enter number of item: "))
retailcost = 0.0
i=0
while(i<noofitems):
    wholesalecost = float(input("enter wholesale cost: "))
    if(wholesalecost<0.0):
        print("invalid negative number entered")
    else:
        retailcost+=wholesalecost*0.5
        i+=1
print(retailcost)
