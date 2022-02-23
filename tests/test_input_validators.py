import unittest
from helpers.InputCommandValidator import validate_input_command, \
    validate_input_args, validate_command_string


class TestInputCommandValidator(unittest.TestCase):
    """Tests to the helper InputCommandValidator"""

    def test_validate_input_command(self):
        """Test to validate de input command validations"""
        self.assertEqual(
            [], validate_input_command(["Q", "a"])
        )
        self.assertEqual(
            ["Q", 1], validate_input_command(["Q", "1"])
        )
        self.assertEqual(
            ["L", 1, 2, 4, 2], validate_input_command(
                ["L", "1", "2", "4", "2"]
            )
        )
        self.assertEqual(
            ["R", 1, 2, 3, 4], validate_input_command(
                ["R", "1", "2", "3", "4"]
            )
        )
        self.assertEqual(
            ["B", 1, 2, "o"], validate_input_command(
                ["B", "1", "2", "o"]
            )
        )

    def test_validate_command_string(self):
        """Test to validate the command string validation"""
        self.assertEqual(True, validate_command_string("L 1 2 3 2"))

    def test_validate_command_string_with_no_string(self):
        """Test to validate the command string validation
        with no parameter given"""
        self.assertEqual(False, validate_command_string(""))

    def test_validate_command_string_with_double_chars(self):
        """Test to validate the command string validation
        with double chars given"""
        self.assertEqual(False, validate_command_string('T1 2 3 4'))

    def test_validate_command_string_with_no_char(self):
        """Test to validate the command string validation
        with no char given"""
        self.assertEqual(False, validate_command_string('1 2 3 4'))

    def test_validate_input_args_with_correct_args(self):
        """Test to validate the input args validation with
        the correct number of arguments provided"""
        self.assertEqual(True, validate_input_args(["Q"]))
        self.assertEqual(True, validate_input_args(["C", 20, 5]))
        self.assertEqual(True, validate_input_args(['L', 1, 2, 3, 2]))
        self.assertEqual(True, validate_input_args(['R', 1, 2, 3, 4]))
        self.assertEqual(True, validate_input_args(['B', 1, 2, 'o']))

    def test_validate_input_args_with_wrong_number_of_args(self):
        """Test to validate the input args validation with
        the wrong number of arguments provided"""
        self.assertEqual(False, validate_input_args(['Q', 1]))
        self.assertEqual(False, validate_input_args(['C', 20]))
        self.assertEqual(False, validate_input_args(['L', 1, 2, 3]))
        self.assertEqual(False, validate_input_args(['R', 1, 2, 3]))
        self.assertEqual(False, validate_input_args(['B', 1]))


if __name__ == '__main__':
    unittest.main()
