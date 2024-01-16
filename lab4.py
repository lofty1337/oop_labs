import time


# Класс команды
class Command:
    def __init__(self, action, description):
        self.action = action
        self.description = description

    def execute(self):
        pass

    def undo(self):
        pass

# Конкретная реализация команды для вывода текста в консоль
class TextCommand(Command):
    def __init__(self, text):
        super().__init__('Print Text', 'Prints text to console')
        self.text = text

    def execute(self):
        print(self.text)

    def undo(self):
        print(f"Undo: {self.text}")

# Виртуальная клавиатура
class VirtualKeyboard:
    def __init__(self):
        self.key_commands = {}
        self.workflow = []

    def assign_command(self, keys, command):
        self.key_commands[keys] = command

    def press_key(self, keys):
        if keys in self.key_commands:
            command = self.key_commands[keys]
            command.execute()
            self.workflow.append(command)
            self.print_workflow()
            return True
        else:
            print(f"No command assigned to keys {keys}")
            return False

    def undo_last_action(self):
        if self.workflow:
            last_command = self.workflow.pop()
            last_command.undo()
            self.print_workflow()

    def print_workflow(self):
        print("Current Workflow:")
        for command in self.workflow:
            print(f"- {command.description}")
        print('\n')


# Пример использования
keyboard = VirtualKeyboard()

# Назначаем команды клавишам
keyboard.assign_command('A', TextCommand("Hello"))
keyboard.assign_command('B', TextCommand("World"))
keyboard.assign_command(('Ctrl', 'C'), TextCommand("Copy"))
keyboard.assign_command(('Ctrl', 'Z'), TextCommand("Undo"))

# Выполняем действия по нажатию клавиш
keyboard.press_key('A')
time.sleep(1)  # Задержка между нажатиями
keyboard.press_key('B')
time.sleep(1)

# Выполняем действия по сочетаниям клавиш
keyboard.press_key(('Ctrl', 'Z'))
time.sleep(1)
keyboard.press_key(('Ctrl', 'C'))

# Откатываем последнюю команду
keyboard.undo_last_action()
