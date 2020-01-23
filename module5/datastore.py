def set_changes(datastore): #this function make changes to a value in department or add new values to it
    changed_department = input("enter department in which you want to change: ") #takes department ex: medical as input
    for i in datastore.keys(): #traverse through keys ex:office
        if(changed_department=="medical"):
            id = int(input("enter room id you want to change: "))
            change = input("enter change you want to make out of {}: ".format(datastore[i][changed_department][id].keys()))
            datastore[i][changed_department][id][change] = input("enter change: ")

        elif(changed_department=="parking"):
            id = int(input("enter parking id you want to change: "))
            change = input("enter change you want to make out of {}: ".format(datastore[i][changed_department][id].keys()))
            datastore[i][changed_department][id][change] = input("enter change: ")
        #if given choice is different from previous
        else :
            id = int(input("enter id you want to change"))
            change = input("enter change: {}".format(datastore[i][changed_department].keys()))
            value = input("enter modified value: ")
            datastore[i][changed_department][change] = value
    return(datastore)

def add_departments(datastore): # this function adds new empty departments to dictonary
    for i in datastore.keys():
        department = input("enter new department you want to add: ")
        datastore[i][department] = {}
    return datastore

def delete_departments(datastore): # this function deletes departments
    departments = input("enter departments: ")
    list_departments = list(departments.split(" "))
    for i in datastore.keys():
        for j in list_departments:
            if(j in datastore[i].keys()):
                del datastore[i][j]
    return datastore
#main function
datastore = {"office": {"medical":{1:{"room-number":100, "use":"reception", "sq-ft":50, "price":75}, 2: {"room-number":101, "use":"waiting", "sq-ft":125, "price":250}, 3: {"room-number":102, "use":"examination", "sq-ft":125, "price":125}},
                        "parking": {1:{"location":"premium", "style": "covered", "price":750}}
                        }}
while(True):
    choice = int(input("enter choice : 1. set changes, 2. add add_departments 3. exit: "))
    if(choice==1):
        datstore = set_changes(datastore)
    elif(choice==2):
        datastore = add_departments(datastore)
    elif(choice==3):
        break
    print(datastore)
