"""class contact:
    def __init__(self,contact_name,contact_number):
        self.contact_name=contact_name
        self.contact_number=contact_number

    def put_data(contact_name,contact_number):
         contact=open("Contact_list","w")
         ccontact_name=self.contact_name
         contact_number=self.contact_number
         contact.write(c_name)
         contact.write(c_number)
         contact.close()
    def get_data(c_name,c_number):
         print("Contact name is ",c_name)
         print("Contact number is ",c_number)
         
contact_name=input("Enter the name")
contact_number=input("Enter the number")
c3=contact(contact_name,contact_number)
print(c3.put_data())
print(c3.get_data())
"""
class contact:
    def __init__(self):
        self.contact_name=input('Enter the name of the contact : ')
        self.phone_no=input('Enter the phone number of the contact : ')
    def put_data(self):
        f=open("phonebook.txt","a")
        f.write(self.contact_name+"   "+self.phone_no+"\n")
        f.close()
        print("Data entered successfully! ")
    def get_data(self):
        f=open("phonebook.txt","r")
        print("The contents of the file are : \n")
        print(f.read())
        f.close()

c1=contact()
c1.put_data()
c1.get_data()
c2=contact()
c2.put_data()
c2.get_data()
