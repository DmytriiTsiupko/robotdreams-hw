import unittest
from io import StringIO
from unittest.mock import patch


def check_chars(input_string=None):
    if input_string is None:
        input_string = input("Please, write something: ")

    for char in input_string:
        if char.isdigit():
            print(f"{char} is a digit", end=" ")
            if int(char) % 2 == 0:
                print(f"and it's an even number")
            else:
                print(f"and it's an odd number")
        elif char.isalpha():
            print(f"{char} is a string", end=" ")
            if char.isupper():
                print("and it's a capital letter")
            else:
                print("and it's a small letter")
        else:
            print(f"{char} is a symbol")


class CheckCharsTestCase(unittest.TestCase):
    @patch('builtins.input', return_value='Hello')
    @patch('sys.stdout', new_callable=StringIO)
    def test_check_chars(self, mock_stdout, _):
        check_chars()

        expected_output = "H is a string and it's a capital letter\n" \
                          "e is a string and it's a small letter\n" \
                          "l is a string and it's a small letter\n" \
                          "l is a string and it's a small letter\n" \
                          "o is a string and it's a small letter\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()




