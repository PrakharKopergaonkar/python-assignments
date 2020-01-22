string = input("enter a string: ")
list = sorted(set(list(string.split(" "))))
for i in list:
    print(i, end=" ")
