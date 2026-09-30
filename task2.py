def get_cats_info(path):
    cats = []  # Список для зберігання словників котів

    try:
        # Відкриваємо файл для читання.
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                # Прибираємо пробіли по краях і перенос рядка.
                line = line.strip()

                # Пропускаємо порожні рядки.
                if not line:
                    continue

                # Розділяємо рядок на ідентифікатор, ім'я та вік.
                cat_id, name, age = line.split(",")

                # Створюємо словник одного кота.
                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                # Додаємо словник до списку.
                cats.append(cat)

        # Повертаємо список після читання всього файлу.
        return cats

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return []

    except (OSError, UnicodeError, ValueError):
        print("Помилка: не вдалося прочитати файл або дані неправильні.")
        return []


# Викликаємо функцію та виводимо результат.
cats_info = get_cats_info("cats.txt")
print(cats_info)