size = int(input("enter size of array: "))
print("enter array")
array = [int(input()) for i in range(0,size)]
sum = int(input("enter sum: "))
list = []
for i in array:
    if(sum-i in list):
        print("pair exist")
        break
    else:
        list.append(i)
