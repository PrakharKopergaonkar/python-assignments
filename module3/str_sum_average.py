string = "English = 78 Science = 83 math = 68 history = 65"
sum=0
list1 = ['0', '1', '2', '3', '4', '5', '6', '7','8', '9']
for i in string.split(" "):
    integer = ""
    for j in i:
        if(j in list1):
            integer+=j
        else:
            integer=""
            break
    if(integer!=""):
        sum+=int(integer)
print("sum is: {} and avg is: {}".format(sum, sum/4))
