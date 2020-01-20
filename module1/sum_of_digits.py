number = int(input("enter a 5 digits number"))
sum=0
count=0
while(number!=0):
    sum+=number%10
    number = int(number/10)
    count+=1
if(count==5):
    print("the sum of digits is : {}".format(sum))
          
else:
    print("the given number is not a 5 digit number")
