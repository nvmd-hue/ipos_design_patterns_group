class User:
    def __init__(self, name):
        self.name = name


class Admin(User):
    pass


class Editor(User):
    pass


class Viewer(User):
    pass


def create_user(user_type: str = "", name: str = "") -> User | None:
    if user_type == "" or name == "":
        return None

    if user_type == "admin":
        return Admin(name)
    elif user_type == "editor":
        return Editor(name)
    elif user_type == "viewer":
        return Viewer(name)

    return None

