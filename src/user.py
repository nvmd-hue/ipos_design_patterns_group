"""This module contains the main User class and subclasses of different
types of users."""

class User:
    """Represent a user in a document management system.

    Attributes:
        name(str): The name of the user.
    """

    def __init__(self, name):
        """Initialise a User instance.

        Args:
            name (str): The name of the user.
        """
        self.name = name


class Admin(User):
    """Represent an administrator user."""
    pass


class Editor(User):
    """Represent an editor user"""
    pass


class Viewer(User):
    """Represent a viewer user."""
    pass


def create_user(user_type: str = "", name: str = "") -> User | None:
    """Create a user instance based on the specified user type.

    Args:
        user_type (str): The role of the user to create.
            Accepted values are 'admin', 'editor' and 'viewer'.
        name (str): The name assigned to the user.

    Returns:
        User | None: An instance of the appropriate User subclass, or None
        if the inputs are missing or the user type is invalid.
    """
    if user_type == "" or name == "":
        return None

    if user_type == "admin":
        return Admin(name)
    elif user_type == "editor":
        return Editor(name)
    elif user_type == "viewer":
        return Viewer(name)

    return None
