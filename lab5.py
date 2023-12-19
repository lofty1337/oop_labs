import json


class User:
    def __init__(self, user_id, name, login, password):
        self._user_id = user_id
        self._name = name
        self._login = login
        self._password = password

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password


class IUserManager:
    def login(self, login, password):
        pass

    def logout(self):
        pass

    def is_authenticated(self):
        pass


class IDataRepository:
    def get(self, item_id):
        pass

    def add(self, item):
        pass

    def delete(self, item_id):
        pass

    def update(self, item):
        pass


class IUserRepository(IDataRepository):
    def find_by_id(self, user_id):
        pass

    def find_by_name(self, name):
        pass


class FileUserManager(IUserManager):
    def __init__(self, user_repository):
        self._current_user = None
        self._user_repository = user_repository

    def login(self, login, password):
        user = self._user_repository.find_by_login(login)
        if user and user.password == password:
            self._current_user = user
            print(f"Welcome, {user.name}! You are now logged in.")
        else:
            print("Invalid login or password.")

    def logout(self):
        if self._current_user:
            print(f"Goodbye, {self._current_user.name}!")
            self._current_user = None
        else:
            print("You are not logged in.")

    def is_authenticated(self):
        return self._current_user is not None

    def register(self, name, login, password):
        if self._user_repository.find_by_login(login):
            print("User with this login already exists. Please choose a different login.")
        else:
            new_user = User(len(self._user_repository._users) + 1, name, login, password)
            self._user_repository.add(new_user)
            print(f"Registration successful! Welcome, {name}!")


class FileUserRepository(IUserRepository):
    def __init__(self, file_path):
        self._file_path = file_path
        self._users = []
        self._load_users()

    def _load_users(self):
        try:
            with open(self._file_path, 'r') as file:
                user_data = json.load(file)
                self._users = [User(**data) for data in user_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self._users = []

    def _save_users(self):
        with open(self._file_path, 'w') as file:
            user_data = [{'user_id': user.user_id, 'name': user.name, 'login': user.login, 'password': user.password}
                         for user in self._users]
            json.dump(user_data, file)

    def find_by_login(self, login):
        for user in self._users:
            if user.login == login:
                return user
        return None

    def find_by_id(self, user_id):
        for user in self._users:
            if user.user_id == user_id:
                return user
        return None

    def find_by_name(self, name):
        for user in self._users:
            if user.name == name:
                return user
        return None

    def add(self, user):
        self._users.append(user)
        self._save_users()


if __name__ == "__main__":
    file_user_repository = FileUserRepository("users.txt")
    file_user_manager = FileUserManager(file_user_repository)
    file_user_manager.login('lofty', '1337')
    # Автоматический вход, если пользователь уже авторизован
    if file_user_manager.is_authenticated():
        print(f"Auto-login: Welcome back, {file_user_manager.current_user.name}!")
    else:
        # Вход, регистрация нового пользователя или смена пользователя
        login_choice = input("Do you want to login, register, or switch user? (login/register/switch): ").lower()

        if login_choice == "login":
            login = input("Enter your login: ")
            password = input("Enter your password: ")
            file_user_manager.login(login, password)
        elif login_choice == "register":
            name = input("Enter your name: ")
            login = input("Enter your login: ")
            password = input("Enter your password: ")
            file_user_manager.register(name, login, password)
        elif login_choice == "switch":
            new_user_name = input("Enter the name of the user you want to switch to: ")
            new_user = file_user_repository.find_by_name(new_user_name)
            if new_user:
                file_user_manager.current_user = new_user
                print(f"Switched to user: {new_user.name}")
            else:
                print(f"User {new_user_name} not found.")
