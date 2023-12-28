from abc import ABC, abstractmethod

# Абстрактный базовый класс контрола
class Control(ABC):
    def __init__(self):
        self.position = (0, 0)

    @abstractmethod
    def set_position(self, x, y):
        self.position = (x, y)

    @abstractmethod
    def get_position(self):
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
class ControlFactory(ABC):
    @abstractmethod
    def create_form(self) -> Form:
        pass

    @abstractmethod
    def create_label(self) -> Label:
        pass

    @abstractmethod
    def create_text_box(self) -> TextBox:
        pass

    @abstractmethod
    def create_combo_box(self) -> ComboBox:
        pass

    @abstractmethod
    def create_button(self) -> Button:
        pass


# Фабрика для Windows
class WindowsControlFactory(ControlFactory):
    def create_form(self) -> Form:
        return WindowsForm()

    def create_label(self) -> Label:
        return WindowsLabel()

    def create_text_box(self) -> TextBox:
        return WindowsTextBox()

    def create_combo_box(self) -> ComboBox:
        return WindowsComboBox()

    def create_button(self) -> Button:
        return WindowsButton()


# Фабрика для Linux
class LinuxControlFactory(ControlFactory):
    def create_form(self) -> Form:
        return LinuxForm()

    def create_label(self) -> Label:
        return LinuxLabel()

    def create_text_box(self) -> TextBox:
        return LinuxTextBox()

    def create_combo_box(self) -> ComboBox:
        return LinuxComboBox()

    def create_button(self) -> Button:
        return LinuxButton()


# Фабрика для MacOS
class MacOSControlFactory(ControlFactory):
    def create_form(self) -> Form:
        return MacOSForm()

    def create_label(self) -> Label:
        return MacOSLabel()

    def create_text_box(self) -> TextBox:
        return MacOSTextBox()

    def create_combo_box(self) -> ComboBox:
        return MacOSComboBox()

    def create_button(self) -> Button:
        return MacOSButton()


# Специфичные для Windows контролы
class WindowsForm(Form):
    def set_position(self, x, y):
        super().set_position(x, y)

    def get_position(self):
        return super().get_position()

class WindowsLabel(Label):
    def set_position(self, x, y):
        super().set_position(x, y)

    def get_position(self):
        return super().get_position()

class WindowsTextBox(TextBox):
    def set_position(self, x, y):
        super().set_position(x, y)

    def get_position(self):
        return super().get_position()

class WindowsComboBox(ComboBox):
    def set_position(self, x, y):
        super().set_position(x, y)

    def get_position(self):
        return super().get_position()

class WindowsButton(Button):
    def set_position(self, x, y):
        super().set_position(x, y)

    def get_position(self):
        return super().get_position()


# Специфичные для Linux контролы
class LinuxForm(Form):
    pass

class LinuxLabel(Label):
    pass

class LinuxTextBox(TextBox):
    pass

class LinuxComboBox(ComboBox):
    pass

class LinuxButton(Button):
    pass


# Специфичные для MacOS контролы
class MacOSForm(Form):
    pass

class MacOSLabel(Label):
    pass

class MacOSTextBox(TextBox):
    pass

class MacOSComboBox(ComboBox):
    pass

class MacOSButton(Button):
    pass


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
