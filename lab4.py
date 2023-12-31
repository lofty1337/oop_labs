import time

# Интерфейс команды
class Command:
    def execute(self):
        pass

    def undo(self):
        pass

# Конкретная команда для действия с клавишей
class KeyActionCommand(Command):
    def __init__(self, keyboard, key, action):
        self.keyboard = keyboard
        self.key = key
        self.action = action

    def execute(self):
        self.keyboard.press_key(self.key, self.action)

    def undo(self):
        print(f"Undoing key action: {self.key}")

# Конкретная команда для действия с комбинацией клавиш
class KeyCombinationCommand(Command):
    def __init__(self, keyboard, combination, action):
        self.keyboard = keyboard
        self.combination = combination
        self.action = action

    def execute(self):
        self.keyboard.press_key_combination(self.combination, self.action)

    def undo(self):
        print(f"Undoing key combination action: {self.combination}")

# Команда для ввода текста
class TypeTextCommand(Command):
    def __init__(self, keyboard, text):
        self.keyboard = keyboard
        self.text = text

    def execute(self):
        for char in self.text:
            self.keyboard.press_key(char, f'Typed: {char}')

    def undo(self):
        print(f"Undoing text typing: {self.text}")

# Команда для стирания текста
class EraseTextCommand(Command):
    def __init__(self, keyboard, text):
        self.keyboard = keyboard
        self.text = text

    def execute(self):
        for char in reversed(self.text):
            self.keyboard.press_key(char, f'Erase: {char}')

    def undo(self):
        print(f"Undoing text erasing: {self.text}")

# Инвокер (в данном случае, сам класс VirtualKeyboard)
class VirtualKeyboard:
    def __init__(self):
        self.command_history = []

    def assign_command(self, command):
        self.command_history.append(command)

    def execute_commands(self):
        for command in self.command_history:
            command.execute()

    def undo_last_command(self):
        if self.command_history:
            command = self.command_history.pop()
            command.undo()

    def press_key(self, key, action):
        print(f"Pressed key '{key}'. Action: {action}")

    def press_key_combination(self, combination, action):
        print(f"Pressed key combination {combination}. Action: {action}")

# Пример использования
keyboard = VirtualKeyboard()

# Создаем команды
type_text_command = TypeTextCommand(keyboard, 'Hello')

erase_text_command = EraseTextCommand(keyboard, 'Hello')


# Назначаем команды клавиатуре
keyboard.assign_command(type_text_command)
keyboard.assign_command(erase_text_command)
time.sleep(1)

# Выполняем команды
keyboard.execute_commands()
time.sleep(1)

# Отменяем последнюю команду
keyboard.undo_last_command()
time.sleep(1)

# Выполняем команды
keyboard.execute_commands()
