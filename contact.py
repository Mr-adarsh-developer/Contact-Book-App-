#empty dictionary
contact = {}

while True:
    print('\n Contact Book App')
    print('1. Create Contact ')
    print('2. View Contact ')
    print('3. Update Contact ')
    print('4. Delete  Contact ')
    print('5. Search Contact ')
    print('6. Count Contact ')
    print('7. Exit  ')

    choice = input("Enter your choice =")

    if choice == '1':
        name = input('Enter your name = ')
        if name in contact:
            print('Contact name{name} already exist')
        else:
            age= input('Enter your age =')
            email= input('Enter your email =')
            mobile= input('Enter your mobile =')
            contact[name]= {'Age': int(age), 'Email':email, 'Mobile': mobile}
            print(f' Contact name {name} has been created successfully!!!')
        
    elif choice=='2':
        name=input('Enter contact name to view =')
        if name in contact:
            contacts=contact[name]
            print(f'Name:{name}, Age:{age}, Mobile number:{mobile}, Email:{email}')
        else:
            print( 'Sorry Contact not found!!')
    elif choice=='3':
        name= input("Enter name to update contact =")
        if name in contact:
            age= input('Enter your  updated age =')
            email= input('Enter your updated email =')
            mobile= input('Enter your updated mobile =')
            contact[name]= {'Age': int(age), 'Email':email, 'Mobile': mobile}
        else:
             print( 'Sorry Contact not found!!')

    elif choice=='4':

        name= input("Enter contact name to delete =")
        if name in contact:
            del contact[name]
            print(f'Contact name{name} has been successfully deleted')
        else:
            print( 'Sorry Contact not found!!')

    elif choice=='5':
        search = input('Enter contact name to search =')
        found=False
        for name, contacts in contact.items():
            if search.lower() in name.lower():
                 print(f'  found - Name:{name}, Age:{age}, Mobile number:{mobile}, Email:{email}')
                 found= True
            if not found:
                     print ('No contact found !!')

    elif choice=='6':
        print(f'Total contact in this App:{ len(contact)}')

    elif choice=='7':
        print('Thank you for visting our site')
        break
    else:
        print('Invalid program ')