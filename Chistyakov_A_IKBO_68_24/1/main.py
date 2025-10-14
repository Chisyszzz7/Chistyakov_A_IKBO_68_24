# demo_script.py
"""
Демонстрационный скрипт для эмулятора командной строки
Этот скрипт демонстрирует работу всех функций эмулятора:
1. Графический интерфейс с правильным заголовком
2. Парсер команд
3. Команды-заглушки ls и cd
4. Команда exit
5. Обработка ошибок
"""

def run_demo():
    print("=== Демонстрация работы эмулятора командной строки ===\n")
    # Имитация работы парсера
    test_commands = [
        "ls",
        "ls -l -a",
        "cd /home/user",
        "cd",
        "unknown_command",
        "exit"
    ]
    def parse_command(command_string):
        parts = command_string.strip().split()
        if not parts:
            return "", []
        command = parts[0]
        args = parts[1:] if len(parts) > 1 else []
        return command, args

    print("1. Демонстрация работы парсера:")
    for cmd in test_commands:
        command, args = parse_command(cmd)
        print(f"   Ввод: '{cmd}' -> Команда: '{command}', Аргументы: {args}")
    print("\n2. Демонстрация выполнения команд:")

    # Имитация выполнения команд
    commands_execution = [
        ("ls", []),
        ("ls", ["-l", "-a"]),
        ("cd", ["/home/user"]),
        ("cd", []),
        ("unknown_command", []),
        ("exit", [])
    ]
    for command, args in commands_execution:
        if command == "ls":
            output = f"Команда: ls\n"
            if args:
                output += f"Аргументы: {', '.join(args)}\n"
            else:
                output += "Аргументы: отсутствуют\n"
            print(f"   Выполнение: {command} {args}")
            print(f"   Результат:\n{output}")

        elif command == "cd":
            output = f"Команда: cd\n"
            if args:
                output += f"Аргументы: {', '.join(args)}\n"
            else:
                output += "Аргументы: отсутствуют\n"
            print(f"   Выполнение: {command} {args}")
            print(f"   Результат:\n{output}")

        elif command == "exit":
            print(f"   Выполнение: {command} {args}")
            print("   Результат: Завершение работы эмулятора...")
        else:
            print(f"   Выполнение: {command} {args}")
            print(f"   Результат: Ошибка: команда '{command}' не найдена")

    print("\n3. Демонстрация обработки ошибок:")
    error_cases = [
        "",  # пустая команда
        "   ",  # только пробелы
        "command_with_many    spaces",  # много пробелов
    ]

    for case in error_cases:
        command, args = parse_command(case)
        print(f"   Ввод: '{case}' -> Команда: '{command}', Аргументы: {args}")

if __name__ == "__main__":
    run_demo()