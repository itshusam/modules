import re

def add_contact(contacts):

    def is_valid_email(email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    print("Please enter the contact information:")
    while True:
        email_address = input("Enter email address: ")
        if is_valid_email(email_address):
            break
        else:
            print("Please enter a valid email address")

    name = input("Enter the name: ")
    phone_number = input("Enter phone number: ")
    additional_info = input("Enter any additional information: ")

    new_contact = {
        "Name": name,
        "Phone number": phone_number,
        "Additional information": additional_info
    }
    contacts[email_address] = new_contact
    print("Contact added successfully!")
    return contacts


def print_contacts(contacts):
    print("contacts:")
    for email, contact_info in contacts.items():
        print(f"Email: {email}")
        for key, value in contact_info.items():
            print(f"{key}: {value}")
        print()


def delete_contact(contacts):
    try:
        email_to_delete = input("Enter the email address of the contact to delete: ")
        if email_to_delete not in contacts:
            raise ValueError("Contact not found.")

        del contacts[email_to_delete]
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Contact deleted successfully!")
    finally:
        return contacts