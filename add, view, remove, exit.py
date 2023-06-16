names = []

def add_name():
    count=int(input("How many names you would like to enter "))
    for i in range(count):
        name=input("Enter the name ")
        names.append(name)
        print("Name added successfully!")

def view_names():
    if len(names) == 0:
        print("The list is empty.")
    else:
        print("Names:")
        for name in names:
            print(name)

def remove_name():
    if len(names) == 0:
        print("The list is empty.")
    else:
        name = input("Enter the name to remove: ")
        if name in names:

            names.remove(name)
            print("Name removed successfully!")
        else:
            print("Name not found in the list.")

def exit():
    print("Thanking You")
    

while True:
    print("1. Add a name")
    print("2. View names")
    print("3. Remove a name")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        add_name()
    elif choice == "2":
        view_names()
    elif choice == "3":
        remove_name()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice, Please Choose Range 1 to 4, Try Again...")
