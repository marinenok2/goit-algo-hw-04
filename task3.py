import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)


def show_directory(path, indent=""):
    for item in path.iterdir():
        if item.is_dir():
            print(Fore.BLUE + f"{indent}Папка: {item.name}")

            # Показуємо вміст цієї папки з більшим відступом.
            show_directory(item, indent + "    ")
        else:
            print(Fore.GREEN + f"{indent}Файл: {item.name}")

# Перевіряємо, чи передали шлях під час запуску.
if len(sys.argv) != 2:
    print('Вкажи шлях: python task3.py "test_folder"')
else:
    path = Path(sys.argv[1])

    try:
        if not path.exists():
            print("Помилка: такого шляху не існує.")
        elif not path.is_dir():
            print("Помилка: потрібно вказати папку, а не файл.")
        else:
            print(Fore.BLUE + f"Папка: {path.resolve().name}")
            show_directory(path, "    ")

    except OSError:
        print("Помилка: не вдалося прочитати вміст папки.")