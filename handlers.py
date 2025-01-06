from address_book import AddressBook
from record import Record

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Not enough arguments provided."
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return wrapper

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact updated."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")
    record.add_birthday(birthday)
    return f"Birthday added for {name}."

@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if record is None or not record.birthday:
        return "No birthday found for this contact."
    return f"{name}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}"

@input_error
def birthdays(args, book: AddressBook):
    days = int(args[0]) if args else 7
    upcoming = book.get_upcoming_birthdays(days)
    if not upcoming:
        return "No upcoming birthdays."
    return "\n".join([f"{name}: in {days_left} days" for name, days_left in upcoming])

@input_error
def change_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")
    if phone:
        record.add_phone(phone)
    return "Contact updated."

@input_error
def show_phones(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if record is None or not record.phones:
        return "No phones found for this contact."
    return "\n".join([phone.value for phone in record.phones])

@input_error
def show_all(book: AddressBook):
    if not book.data:
        return "No contacts found."
    return "\n".join([str(record) for record in book.data])