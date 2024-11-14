#contact management system
import json
import os

# Path to store contacts in a JSON file
FILE_PATH = 'contacts.json'

# Load contacts from the file
def load_contacts():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    else:
        return {}

# Save contacts to the file
def save_contacts(contacts):
    with open(FILE_PATH, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    if name in contacts:
        print("Contact already exists!")
        return

    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for name, details in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")

# Update an existing contact
def update_contact(contacts):
    name = input("Enter the contact name to update: ")
    if name not in contacts:
        print("Contact not found!")
        return

    print("Leave blank if you don't want to change a field.")
    phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ") or contacts[name]['phone']
    email = input(f"Enter new email (current: {contacts[name]['email']}): ") or contacts[name]['email']
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print(f"Contact '{name}' updated successfully!")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the contact name to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found!")

# Main menu for the Contact Management System
def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()