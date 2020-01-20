quantity = int(input("enter quantity: "))
discount=0
if(quantity>=100):
    discount = ((99*quantity)*4)/10
elif(quantity>=50):
    discount = ((99*quantity)*3)/10
elif(quantity>=20):
    discount = ((99*quantity)*2)/10
elif(quantity>=10):
    discount = (99*quantity)/10
print("the amount of discount is: {}".format(discount))
discounted_price = (99*quantity) - discount
print("total amount of purchase after the discount: {}".format(discounted_price))
