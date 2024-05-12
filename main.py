from address_book import Record, AddressBook


def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    john.remove_phone("5555555555")  # Видалення телефону 5555555555
    print(john)  # Виведення: Contact name: John, phones: 1112223333

    # Видалення запису Jane
    book.delete("Jane")

    print(book.data)  # Виведення: {'John': <record.Record object at 0x7f8f3c4f4d30>}

    john.add_birthday("15.05.1990")
    book.add_record(john)

    birthdays = book.get_upcoming_birthdays()
    print("Список привітань на цьому тижні:", birthdays)


if __name__ == "__main__":
    main()
