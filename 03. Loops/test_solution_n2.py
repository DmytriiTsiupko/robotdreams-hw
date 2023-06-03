import io
import sys
import unittest
from unittest.mock import patch
import time


def print_love_python():
    time.sleep(4.2)
    print("I love Python")


class TestPrintLovePython(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_love_python(self, mock_stdout):
        with patch('time.sleep') as mock_sleep:
            print_love_python()
            mock_sleep.assert_called_with(4.2)
            self.assertEqual(mock_stdout.getvalue(), "I love Python\n")


if __name__ == "__main__":
    unittest.main()