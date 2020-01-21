n1 = int(input("enter size of first array"))
n2 = int(input("enter size of second array"))
print("enter first list")
list = [int(input()) for i in range(0, n1)]
print("enter second list")
second_list = [int(input()) for i in range(0,n2)]
print(sum(list)-sum(second_list))
