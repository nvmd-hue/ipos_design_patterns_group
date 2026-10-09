import unittest
from user import create_user, Admin, Editor, Viewer


class TestUser(unittest.TestCase):

    def test_admin_user_created(self):

        user_type = "admin"
        name = "Wendy"

        new_user = create_user(user_type, name)

        self.assertIsInstance(new_user, Admin)
        self.assertTrue(new_user.name, "Wendy")

    def test_editor_user_created(self):

        user_type = "editor"
        name = "Jim"

        new_user = create_user(user_type, name)

        self.assertIsInstance(new_user, Editor)
        self.assertTrue(new_user.name, "Jim")

    def test_viewer_user_created(self):

        user_type = "viewer"
        name = "Harry"

        new_user = create_user(user_type, name)

        self.assertIsInstance(new_user, Viewer)
        self.assertTrue(new_user.name, "Harry")

    def test_missing_input_returns_none(self):

        user_type = ""
        name = "Harry"

        new_user = create_user(user_type, name)

        self.assertIsNone(new_user)


if __name__ == "__main__":
    unittest.main()