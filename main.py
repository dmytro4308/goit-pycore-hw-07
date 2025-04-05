from utils import parse_input
from handlers import add_contact, edit_contact, get_contact, birthdays, add_birthday, show_birthday
from address_book import AddressBook

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case x if x in ["close", "exit"]:
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, book))
            case "change":
                print(edit_contact(args, book))
            case "phone":
                print(get_contact(args, book))
            case "all":
                for contact in book:
                    print(contact)
            case "add-birthday":
                print(add_birthday(args, book))
            case "show-birthday":
                print(show_birthday(args, book))
            case "birthdays":
                print(birthdays(args, book))
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()