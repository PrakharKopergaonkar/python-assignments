import pickle
class contactclass:
    def __init__(self, dict, name="", email="", phone=0, id=""):
        self.dict = dict
        self.name = name
        self.email = email
        self.phone = phone
        self.id = id

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_id(self):
        return id

    def set_name(self, x):
        self.name = x

    def set_email(self, x):
        self.email = x

    def set_phone(self, x):
        self.phone = x

    def set_id(self, id):
        self.id = id

    def __str__(self):
        return self.dict[self.get_id()]

    def newcontact(self, id):
        name = input("enter your name: ")
        self.set_name(name)
        email = input("enter your email: ")
        self.set_email(email)
        phone = input("enter your phone: ")
        self.set_phone(phone)
        self.set_id(id)
        self.dict[self.id] = {self.name, self.email, self.phone}

    def lookupcontact(self, id):
        for i in self.dict.keys():
            if(i == id):
                return self.dict[i]
        return "id does not exist"

    def deletecontact(self, id):
        for i in self.dict.keys():
            if(i==id):
                del self.dict[i]
                break
        return "id does not exist"

    def existingcontact(self, id):
        for i in self.dict.keys():
            if(i==id):
                change = input("enter all changes you want to make out of name, email and phone_no")
                list1 = list(change.split(" "))
                for i in list1:
                    if(i=='name'):
                        name = input("enter new name: ")
                        self.set_name(name)
                    elif(i=='email'):
                        email = input("enter new email: ")
                        self.set_email(email)
                    elif(i=='phone_no'):
                        phone_no = int(input("enter new phone_no: "))
                        self.set_phone(phone_no)
                    else:
                        print("parameter doesn't exist")
            else:
                print("id does not exist")
def main():
    dict = {}
    handle = open('lookupdetails.bat', 'rb+')
    while(True):
        contactobject = contactclass(dict)
        choice = int(input("enter your choice: 1. lookupcontact, 2.newcontact, 3.update_existingcontact, 4. deletecontact: "))
        if(choice==1):
            id = int(input("enter id you are looking for"))
            print(contactobject.lookupcontact(id))
        elif(choice==2):
            id = int(input("enter id of newcontact:"))
            contactobject.newcontact(id)
            dict[id] = contactobject
            pickle.dump(dict, handle)
            print(dict)
        elif(choice==3):
            id = int(input("enter id of existing contact:"))
            contactobject.existingcontact(id)
            dict[id] = contactobject
            pickle.dump(dict, handle)
            print(dict)
        elif(choice==4):
            id = int(input("enter id you want to delete"))
            contactobject.deletecontact(id)
            dict = contactobject
            pickle.dump(dict, handle)
        elif(choice==5):
            exit()
        else:
            print("invalid choice")
main()




