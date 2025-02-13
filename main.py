from address_book import AddressBook
from handlers import (
    add_contact,
    change_contact,
    show_phones,
    show_all,
    add_birthday,
    show_birthday,
    birthdays,
)

from pickle_serializer import save_data, load_data

def parse_input(user_input: str):
    parts = user_input.split()
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args

def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        parsed_input = parse_input(user_input)
        if len(parsed_input) == 1:
            command, args = parsed_input[0], []
        else:
            command, args = parsed_input[0], parsed_input[1:]

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phones(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()