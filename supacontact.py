from supabase_client import supabase
total_contacts = supabase.table("contacts").select("*").execute().data

# contacts = []
while True:
    print(" ------Welcome ------")
    print("-------Input Option-----")
    print(f"There are {len(total_contacts)} contacts.")
    # print("Type of response", type(total_contacts))
    print(" Input 1 Create new Contact")
    print(" Input 2 View Existing Contact")
    print(" Input 3  Update Contact")
    print(" Input 4  Delete Contact")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter name: ")
        if(len(name) < 3): 
            print("Name should be atleast 3 character")
            continue
        contacts = supabase.table("contacts").select("*").eq("Name", name).execute()
        if contacts.data:
            print("Name exists")
        else: 
            cell = input("Enter cell: ") 
            new_contact = {"Name": name, "Cell": cell} 
            # contacts.append(new_contact)  //thhis is for list
            supabase.table("contacts").insert(new_contact).execute()
            
            print(f"Contact {name} added sucessfully")
    
    if choice == "2":
        name = input("Enter name to view: ") 
        contacts = supabase.table("contacts").select("*").eq("Name", name).execute()
        if contacts.data:
            print("Name exists") 
        else:
            print(f"contact {name} does not exist")  
            
    if choice == "3" :
        name = input("Enter name to update:")
        contacts = supabase.table("contacts").select("*").eq("Name", name).execute()
        if contacts.data:
            print("Name exists") 
        else:
            cell = input("Enter cell: ") 
            updated_contact = {"Name": name, "Cell": cell} 
            supabase.table("contacts").insert(updated_contact).execute()
            print(f"Contact {name} updated sucessfully")
            
    if choice == "4":
        name = input("Enter name to delete:")
        contacts = supabase.table("contacts").select("*").eq("Name", name).execute()
        if contacts.data:
            print(f"contact {name} deleted suceesfully")
        else:
            print(f"contact {name} doesnt exist")    
            
                     
               
                 
               
              
            
            
    else:
        break            
    