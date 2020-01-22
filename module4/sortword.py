string = input("enter a string: ")
list = sorted(set(string.split(" ")))
for i in list:
    print(i, end=" ")
