def total_salary(path):
    total = 0  # Загальна сума зарплат
    count = 0  # Кількість працівників

    try:
        # Відкриваємо файл. with автоматично закриє його.
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                # Прибираємо пробіли по краях і перенос рядка.
                line = line.strip()

                # Пропускаємо порожні рядки.
                if not line:
                    continue

                # Відділяємо ім'я від зарплати.
                name, salary = line.split(",")

                # Перетворюємо зарплату на число.
                salary = int(salary)

                # Накопичуємо суму та рахуємо працівників.
                total += salary
                count += 1

        # У порожньому файлі немає зарплат.
        if count == 0:
            return 0, 0

        average = total / count

        # Повертаємо два числа — кортеж.
        return total, average

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return 0, 0

    except (OSError, UnicodeError, ValueError):
        print("Помилка: не вдалося прочитати файл або дані неправильні.")
        return 0, 0


# Викликаємо функцію й отримуємо два результати.
total, average = total_salary("salary.txt")

print(f"Загальна сума заробітної плати: {total}")
print(f"Середня заробітна плата: {average}")
