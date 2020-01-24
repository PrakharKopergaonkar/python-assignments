import pickle #pickle reading and writing should be used
def add_contents_to_departments(datastore):
    for i in datastore.keys():
        try:
            department = input("enter department you want to add content to: ")
            keys = input("enter attributes you want to add: ")
            id = int(input("enter id you want add keys to: "))
            listkeys = list(keys.split(" "))
            for j in listkeys:
                value = input("enter data you want to {} key: ".format(j))
                datastore[i][department][id][j] = value
        except KeyError:
            print("enter valid department")
    return datastore #this adds content to existing departments

def set_changes(datastore): #this function make changes to a value in department or add new values to it
    changed_department = input("enter department in which you want to change: ") #takes department ex: medical as input
    for i in datastore.keys(): #traverse through keys ex:office
        while(True):
            try:
                id = int(input("enter {} id you want to change: ".format(changed_department)))
                change = input("enter change you want to make out of {}: ".format(datastore[i][changed_department][id].keys()))
                datastore[i][changed_department][id][change] = input("enter change: ")
                break
            except ValueError:
                print("enter valid input")
            except KeyError:
                print("enter valid id")
    return(datastore)

def add_departments(datastore): # this function adds new empty departments to dictonary
    for i in datastore.keys():
        department = str(input("enter new department you want to add: "))
        datastore[i][department] = {}
    return datastore

def delete_departments(datastore): # this function deletes departments
    for i in datastore.keys():
        departments = input("enter department out of {}: ".format(datastore[i].keys()))
        while(True):
            try:
                del datastore[i][j]
                break
            except KeyError:
                print("enter valid department")
    return datastore


def main(): #main function
    datastore = {"office": {"medical":{1:{"room-number":100, "use":"reception", "sq-ft":50, "price":75}, 2: {"room-number":101, "use":"waiting", "sq-ft":125, "price":250}, 3: {"room-number":102, "use":"examination", "sq-ft":125, "price":125}},
                        "parking": {1:{"location":"premium", "style": "covered", "price":750}}
                        }}
    while(True):
        choice = int(input("enter choice : 1. set changes, 2. add_departments 3. add contents to departments 4. delete department 4. exit "))
        if(choice==1):
            datstore = set_changes(datastore)
        elif(choice==2):
            datastore = add_departments(datastore)
        elif(choice==3):
            datastore = add_contents_to_departments(datastore)
        elif(choice==4):
            datastore = delete_departments(datastore)
        elif(choice==5):
            exit()
        else :
            print("invalid choice")
        print(datastore)
        with open('data.pickle', 'wb') as handle:
            pickle.dump(datastore, handle)
main()
