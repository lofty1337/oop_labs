import time


class VirtualKeyboard:
    def __init__(self):
        self.key_actions = {}
        self.key_combinations = {}
        self.history = []

    def assign_key_action(self, key, action):
        self.key_actions[key] = action

    def assign_key_combination(self, combination, action):
        combination = tuple(combination)
        self.key_combinations[combination] = action

    def press_key(self, key):
        if key in self.key_actions:
            action = self.key_actions[key]
            self.history.append(action)
            print(f"Pressed key '{key}'. Action: {action}")
        else:
            print(f"No action assigned to key '{key}'.")

    def press_key_combination(self, combination):
        combination = tuple(combination)
        if combination in self.key_combinations:
            action = self.key_combinations[combination]
            self.history.append(action)
            print(f"Pressed key combination {combination}. Action: {action}")
        else:
            print(f"No action assigned to key combination {combination}.")

    def undo_last_action(self):
        if self.history:
            action = self.history.pop()
            print(f"Undoing last action: {action}")
        else:
            print("No actions to undo.")


# Пример использования
keyboard = VirtualKeyboard()
keyboard.assign_key_action('B', 'Action B')
keyboard.assign_key_combination(['D', 'E'], 'Action DE')

keyboard.press_key('B')
time.sleep(1)
keyboard.press_key_combination(['D', 'E'])
time.sleep(1)

keyboard.undo_last_action()
time.sleep(1)
keyboard.undo_last_action()
time.sleep(1)
keyboard.undo_last_action()
time.sleep(1)
