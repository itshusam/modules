import mood_responses
import contacts_manager
import text_utils as tu

#task 1
mood = input("How are you feeling today? ")
print(mood_responses.mood_response(mood))

contacts={}

#task 2

while True:
    print(
    '''  
    Welcome to the Contact Management System!
    please select one of the following :
    1-Add a new contact
    2-view contacts
    3-Delete a contact
    4-Quit
    '''
    )

    choice = input("")

    if choice == "1":
       contacts_manager.add_contact(contacts)
       
    elif choice == "2":
        contacts_manager.print_contacts(contacts)

    elif choice == "3":
        contacts_manager.delete_contact(contacts)

    elif choice =="4":
        break


#task 3

string="hello coding temple"
tu.capitalize_string(string)
tu.string_reversal(string)