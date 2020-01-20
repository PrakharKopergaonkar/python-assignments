amount = 99
quantity = int(input("enter quantity: "))
discount=0
if(10<=quantity<=19):
    discount = (99*quantity)/10
elif(20<=quantity<=49):
    discount = ((99*quantity)*2)/10
elif(50<=quantity<=99):
    discount = ((99*quantity)*3)/10
elif(quantity>100):
    discount = ((99*quantity)*4)/10
print("the amount of discount is: {}".format(discount))
discounted_price = (99*quantity) - discount
print("total amount of purchase after the discount: {}".format(discounted_price))
