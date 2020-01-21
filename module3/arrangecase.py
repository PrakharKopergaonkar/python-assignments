string = input("enter string")
string1=""
string2=""
for i in string:
    if(i == i.lower()):
        string1+=i
    else:
        string2+=i
print(string1+string2)
