from collections import UserDict

class ContactExistsError(Exception):
    ...

class ContactDoesNotExistError(Exception):
    ...

class PhoneExistsError(Exception):
    ...

class PhoneDoesNotExistError(Exception):
    ...

class AddressBook(UserDict):
    def add_record(self, name: str, phone: str) -> str:
        if name in self.data:
            raise ContactExistsError
        else:
            self.data[name] = Record(name, phone)
            return f'Contact with name {name} and phone {phone} was successfully added!'
    
    def delete_record(self, name: str) -> str:
        if name not in self.data:
            raise ContactDoesNotExistError
        else:
            self.data.pop(name)
            return f'Contact with name {name} was successfully removed!'
    
    def change_record(self, command: str, data: list) -> str:
        if data[0] not in self.data:
            raise ContactDoesNotExistError
        elif command == 'phone':
            result = [i.phone for i in self.data.get(data[0]).phones]
            return result
        else:
            changes = getattr(self.data.get(data[0]), command)
            result = changes(*data[1:])
            return result


class Record:
    def __init__(self, name: str, phone: str) -> None:
        self.name = Name(name)
        self.phones = [Phone(phone)]

    def add(self, user_phone: str) -> str:
        phone_in = list(filter(lambda phone: phone.phone == user_phone, self.phones))
        if phone_in:
            raise PhoneExistsError
        else:
            self.phones.append(Phone(user_phone))
            return f'The phone number {user_phone} was successfully added to contact {self.name.name}!'

    def delete(self, user_phone: str) -> str:
        phone_in = list(filter(lambda phone: phone.phone == user_phone, self.phones))
        if not phone_in:
            raise PhoneDoesNotExistError
        else:
            self.phones.remove(phone_in[0])
            return f'The phone number {user_phone} was successfully removed from contact {self.name.name}!'
    
    def change(self, old_phone: str, new_phone: str) -> str:
        phone_in = list(filter(lambda phone: phone.phone == old_phone, self.phones))
        if not phone_in:
            raise PhoneDoesNotExistError
        else:
            phone_in[0].phone = new_phone
            return f'The phone number {old_phone} in contact {self.name.name} was successfully changed to {new_phone}'


class Field:
    ...


class Name:
    def __init__(self, name) -> None:
        self.name = name


class Phone:
    def __init__(self, phone) -> None:
        self.phone = phone


