contacts = {}

while True:
    print("\n Welcome to Contact Details")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Updata Contact ")
    print("4. Count Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        if name in contacts:
            print("Contact already exists")
        else:
            email = input("Enter your email: ")
            cell = input("Enter your cell: ")
            contacts[name] = {"email": email, "cell": cell}
            print(f"Contace name {name} added sucessfully")
            
    elif choice == "2":
            name = input("Enter name to view: ")
            if name in contacts:
                print(f"Contact name: {name} {contacts[name]}")
                # print(f"Email: {contacts[name]["email"]}")
                
            else:
                print(f"contact name {name} doesnt exist")
                
            #  name = input("Enter name ")
             
    elif choice == "3":
        name = input("Enter name to update :")
        
        
        if name in contacts:
            name = input("Enter name you wanna update: ")
            email = input("Enter email you wanna update: ")
            cell = input("Enter cell you wanna update: ")
            contacts[name] = {"email": email, "cell": cell}
            print(f"contact name {name} updated successfully")
        else:
            print(f"contact name {name} doesnt exist")  
            
    elif choice == "4":
        print(f"Total contacts is: {len(contacts)}")  
        
    elif choice == "5":
        name = input("Enter name to delete: ") 
        if name in contacts:
            print(f"contact name {namme} has been deleted") 
        else:
            print(f"contact name {name} not found")              
    else: 
        break
            
    
    
    
    
                 
    
                
            
        
        
        
            



