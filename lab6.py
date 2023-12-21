# Базовый класс Control
class Control:
    def __init__(self):
        self.position = (0, 0)

    def set_position(self, x, y):
        self.position = (x, y)
        print(f"Вызван метод set_position у контролла {type(self).__name__} с координатами {self.position}")

    def get_position(self):
        print(f"Вызван метод get_position у контролла {type(self).__name__}")
        return self.position


# Контрол для формы
class Form(Control):
    def __init__(self):
        super().__init__()
        self.controls = []

    def add_control(self, control):
        self.controls.append(control)
        print(f"Вызван метод add_control у формы. Добавлен контролл {type(control).__name__}")

    def get_controls(self):
        return self.controls


# Контрол для метки
class Label(Control):
    def __init__(self):
        super().__init__()
        self.text = ""

    def set_text(self, text):
        self.text = text
        print(f"Вызван метод set_text у метки. Установлен текст: {text}")

    def get_text(self):
        print(f"Вызван метод get_text у метки")
        return self.text


# Контрол для текстового поля
class TextBox(Control):
    def __init__(self):
        super().__init__()
        self.text = ""

    def set_text(self, text):
        self.text = text
        print(f"Вызван метод set_text у текстового поля. Установлен текст: {text}")

    def get_text(self):
        print(f"Вызван метод get_text у текстового поля")
        return self.text

    def on_value_changed(self):
        print(f"Вызван метод on_value_changed у текстового поля")


# Контрол для комбо-бокса
class ComboBox(Control):
    def __init__(self):
        super().__init__()
        self.items = []
        self.selected_index = -1

    def get_selected_index(self):
        print(f"Вызван метод get_selected_index у комбо-бокса")
        return self.selected_index

    def set_selected_index(self, index):
        self.selected_index = index
        print(f"Вызван метод set_selected_index у комбо-бокса. Установлен индекс: {index}")

    def set_items(self, items):
        self.items = items
        print(f"Вызван метод set_items у комбо-бокса. Установлены элементы: {items}")

    def get_items(self):
        print(f"Вызван метод get_items у комбо-бокса")
        return self.items


# Контрол для кнопки
class Button(Control):
    def __init__(self):
        super().__init__()
        self.text = ""

    def set_text(self, text):
        self.text = text
        print(f"Вызван метод set_text у кнопки. Установлен текст: {text}")

    def get_text(self):
        print(f"Вызван метод get_text у кнопки")
        return self.text

    def click(self):
        print(f"Вызван метод click у кнопки")


# Абстрактная фабрика
class ControlFactory:
    def create_form(self):
        pass

    def create_label(self):
        pass

    def create_text_box(self):
        pass

    def create_combo_box(self):
        pass

    def create_button(self):
        pass


# Фабрика для Windows
class WindowsControlFactory(ControlFactory):
    def create_form(self):
        return Form()

    def create_label(self):
        return Label()

    def create_text_box(self):
        return TextBox()

    def create_combo_box(self):
        return ComboBox()

    def create_button(self):
        return Button()


# Фабрика для Linux
class LinuxControlFactory(ControlFactory):
    def create_form(self):
        return Form()

    def create_label(self):
        return Label()

    def create_text_box(self):
        return TextBox()

    def create_combo_box(self):
        return ComboBox()

    def create_button(self):
        return Button()


# Фабрика для MacOS
class MacOSControlFactory(ControlFactory):
    def create_form(self):
        return Form()

    def create_label(self):
        return Label()

    def create_text_box(self):
        return TextBox()

    def create_combo_box(self):
        return ComboBox()

    def create_button(self):
        return Button()


# Пример использования
def main():
    # Выбираем фабрику в зависимости от ОС (здесь просто для примера выбрана Windows)
    factory = WindowsControlFactory()

    # Создаем форму
    form = factory.create_form()

    # Создаем и добавляем контроллы на форму
    label = factory.create_label()
    textbox = factory.create_text_box()
    combobox = factory.create_combo_box()
    button = factory.create_button()

    form.add_control(label)
    form.add_control(textbox)
    form.add_control(combobox)
    form.add_control(button)

    # Вызываем методы контролов
    label.set_text("Hello, World!")
    textbox.set_text("Input text")
    textbox.on_value_changed()
    combobox.set_items(["Option 1", "Option 2", "Option 3"])
    combobox.get_selected_index()
    button.set_text("Click me")
    button.click()

    # Выводим позиции всех контролов
    for control in form.get_controls():
        control.set_position(10, 20)
        print(f"Позиция контролла {type(control).__name__}: {control.get_position()}")


if __name__ == "__main__":
    main()
