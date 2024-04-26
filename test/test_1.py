import unittest
import sys
import os
from unittest.mock import patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from smartshop.code.viewer import start_window


class TestStartWindow(unittest.TestCase):

    @patch('start_window.UI_main_window.__init__')
    def test_init(self, mock_init):
        start_window.UI_main_window.__init__()
        mock_init.assert_called()


if __name__ == '__main__':
    unittest.main()
