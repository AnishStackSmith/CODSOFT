contacts = []

def display_menu():
    print("\n📘 Contact Book Menu")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print("✅ Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\n📋 Contact List:")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} - {c['phone']}")

def search_contact():
    keyword = input("🔍 Enter name or phone number to search: ").lower()
    found = False
    for c in contacts:
        if keyword in c["name"].lower() or keyword in c["phone"]:
            print("\n📇 Contact Found:")
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}")
            found = True
            break
    if not found:
        print("❌ No contact found.")

def update_contact():
    search_name = input("Enter the name of the contact to update: ").lower()
    for c in contacts:
        if c["name"].lower() == search_name:
            print("Enter new details (leave blank to keep existing):")
            new_phone = input(f"New Phone [{c['phone']}]: ") or c["phone"]
            new_email = input(f"New Email [{c['email']}]: ") or c["email"]
            new_address = input(f"New Address [{c['address']}]: ") or c["address"]
            c["phone"] = new_phone
            c["email"] = new_email
            c["address"] = new_address
            print("✅ Contact updated.")
            return
    print("❌ Contact not found.")

def delete_contact():
    search_name = input("Enter the name of the contact to delete: ").lower()
    for i, c in enumerate(contacts):
        if c["name"].lower() == search_name:
            confirm = input(f"Are you sure you want to delete '{c['name']}'? (yes/no): ").lower()
            if confirm == "yes":
                del contacts[i]
                print("🗑️ Contact deleted.")
            else:
                print("Deletion cancelled.")
            return
    print("❌ Contact not found.")

# Main loop
def run_contact_book():
    print("📒 Welcome to Contact Book")
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

# Start the program
run_contact_book()
