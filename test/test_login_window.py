import sys
import unittest
from pathlib import Path
from unittest.mock import Mock
from unittest.mock import patch

script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir.parent.parent))

from smartshop.code.viewer.py import login_window


class TestLoginWindow(unittest.TestCase):
    def setUp(self):
        self.login_window = login_window.LoginWindow()
        self.login_window.username = Mock()
        self.login_window.password = Mock()
        self.login_window.database = Mock()
        self.login_window.error_message = Mock()

    @patch("login_window.start_window.UIMainWindow")
    def test_check_login_success(self, mock_start_window):
        self.login_window.username.text.return_value = "test_user"
        self.login_window.password.text.return_value = "test_password"
        self.login_window.database.get_password_hash.return_value = "hashed_password"
        self.login_window.compare_password.return_value = True

        self.login_window.login_user()

        mock_start_window.assert_called_once_with("test_user")
        mock_start_window.return_value.set_up_start_menu.assert_called_once()
        self.login_window.error_message.assert_not_called()

    @patch("login_window.start_window.UIMainWindow")
    def test_check_login_failure(self, mock_start_window):
        self.login_window.username.text.return_value = "test_user"
        self.login_window.password.text.return_value = "wrong_password"
        self.login_window.database.get_password_hash.return_value = "hashed_password"
        self.login_window.compare_password.return_value = False

        self.login_window.login_user()

        mock_start_window.assert_not_called()
        self.login_window.error_message.assert_called_once()


if __name__ == "__main__":
    unittest.main()
