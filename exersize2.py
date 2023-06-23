def func1(dict):
    """Adds a new contact"""
    name = input('\nEnter name:')
    phone = int(input('Enter phone number:'))
    dict[name] = phone
    print('\nContact added successfully!')
    

def func2(dict):
    """Searches for a contact"""
    name = input('\nEnter name:')
    print('Phone number: ', dict[name])


def func3(dict):
    """Lists all contacts"""
    print('Contacts')
    for key, value in dict.items():
        print(key, ': ', value)


print('Phone Book Program\n-----------------\n1. Add a new contact')
print('2. Search for a contact\n3. List all contacts\n4. Exit')
d = {}
while True:
    i = int(input('\nEnter your choice:'))
    if i == 1:
        func1(d)
    elif i == 2:
        func2(d)
    elif i == 3:
        func3(d)
    else:
        print('\nGoodbye!')
        break
