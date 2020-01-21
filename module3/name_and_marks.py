string = input("enter data")
list = string.split(',')
theorysum=0
for i in list[1:6]:
    theorysum+=int(i)
practicalsum=0
for i in list[6:9]:
    practicalsum+=int(i)
percentage = ((theorysum+practicalsum)*100)/650
print(list[0]+" obtained "+str(theorysum)+" out of 500 in theory and "+str(practicalsum)+" out of 90 in practical and succesfully passed the exam with"+str(percentage)+ "in aggregate")
