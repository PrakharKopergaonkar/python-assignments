string = "English = 78 Science = 83 math = 68 history = 65"
sum=0
def isint(i):
    try:
        num = int(i)
    except ValueError:
        return False
    return True
for i in string.split(" "):
    if(isint(i)):
        sum+=int(i)
print("sum is: {} and avg is: {}".format(sum, sum/4))

