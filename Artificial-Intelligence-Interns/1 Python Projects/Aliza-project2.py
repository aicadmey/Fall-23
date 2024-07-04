import json

class AddressBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                contacts = json.load(file)
            return contacts
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, email, phone):
        contact = {'name': name, 'email': email, 'phone': phone}
        self.contacts.append(contact)
        self.save_contacts()
        print(f'Contact for {name} added.')

    def list_contacts(self):
        if not self.contacts:
            print('Address book is empty.')
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}")

    def search_contact(self, name):
        matching_contacts = [contact for contact in self.contacts if name in contact['name']]
        if not matching_contacts:
            print('No matching contacts found.')
        else:
            print(f'Matching contacts for "{name}":')
            for i, contact in enumerate(matching_contacts, 1):
                print(f"{i}. Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}")

    def edit_contact(self, index, new_name, new_email, new_phone):
        if 1 <= index <= len(self.contacts):
            contact = self.contacts[index - 1]
            contact['name'] = new_name
            contact['email'] = new_email
            contact['phone'] = new_phone
            self.save_contacts()
            print('Contact updated successfully.')
        else:
            print('Invalid contact index.')

    def delete_contact(self, index):
        if 1 <= index <= len(self.contacts):
            deleted_contact = self.contacts.pop(index - 1)
            self.save_contacts()
            print(f'Contact for {deleted_contact["name"]} deleted.')
        else:
            print('Invalid contact index.')

def main():
    address_book = AddressBook("address_book.json")

    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Save and Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            email = input("Enter contact email: ")
            phone = input("Enter contact phone: ")
            address_book.add_contact(name, email, phone)
        elif choice == "2":
            address_book.list_contacts()
        elif choice == "3":
            name = input("Enter the name to search: ")
            address_book.search_contact(name)
        elif choice == "4":
            index = int(input("Enter the index of the contact to edit: "))
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            phone = input("Enter new phone: ")
            address_book.edit_contact(index, name, email, phone)
        elif choice == "5":
            index = int(input("Enter the index of the contact to delete: "))
            address_book.delete_contact(index)
        elif choice == "6":
            print("Saving and exiting.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
