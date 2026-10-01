# Розбираємо введений текст на команду та аргументи
def parse_input(user_input):
    words = user_input.split()

    # Якщо користувач нічого не ввів
    if not words:
        return "", []

    command, *args = words
    command = command.lower()

    return command, args


# Додаємо контакт
def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Use: add name phone"

    name, phone = args
    name = name.lower()

    contacts[name] = phone

    return "Contact added."


# Змінюємо телефон наявного контакту
def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Use: change name phone"

    name, phone = args
    name = name.lower()

    if name not in contacts:
        return "Contact not found."

    contacts[name] = phone

    return "Contact updated."


# Показуємо телефон за ім'ям
def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Use: phone name"

    name = args[0].lower()

    if name not in contacts:
        return "Contact not found."

    return contacts[name]


# Показуємо всі контакти
def show_all(contacts):
    if not contacts:
        return "No contacts."

    result = ""

    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"

    return result.rstrip()


# Основна функція: введення команд і показ відповідей
def main():
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"] and not args:
            print("Good bye!")
            break

        elif command == "hello" and not args:
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all" and not args:
            print(show_all(contacts))

        else:
            print("Invalid command.")


# Запускаємо бота, коли запускаємо цей файл
if __name__ == "__main__":
    main()
