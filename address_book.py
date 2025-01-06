from collections import UserDict
from record import Record

class AddressBook(UserDict):
    def find(self, name: str) -> Record:
        return self.data.get(name)
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record
        
    def iterator(self, item):
        return item

    def get_upcoming_birthdays(self, days: int):
        return {
            name: record.days_to_birthday()
            for name, record in self.data.items()
            if record.days_to_birthday() is not None and record.days_to_birthday() <= days
        }