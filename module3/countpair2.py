def countpairs(list1, list2, sum):
    count = 0
    for i in list1:
        if(sum - i in list2):
            count+=1
    return count
size1 = int(input("enter size of first list: "))
print("enter first list :")
list1 = [int(input()) for i in range(0,size1)]
size2 = int(input("enter size of second list: "))
print("enter second list: ")
list2 = [int(input()) for i in range(0, size2)]
sum = int(input("enter sum: "))
print(countpairs(list1,list2,sum))
