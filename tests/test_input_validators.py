import unittest
from helpers.InputCommandValidator import validate_input_command, \
    validate_input_args, validate_command_string, validate_file_name


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
        self.assertTrue(validate_command_string("L 1 2 3 2"))

    def test_validate_command_string_with_no_string(self):
        """Test to validate the command string validation
        with no parameter given"""
        self.assertFalse(validate_command_string(""))

    def test_validate_command_string_with_double_chars(self):
        """Test to validate the command string validation
        with double chars given"""
        self.assertFalse(validate_command_string('T1 2 3 4'))

    def test_validate_command_string_with_no_char(self):
        """Test to validate the command string validation
        with no char given"""
        self.assertFalse(validate_command_string('1 2 3 4'))
        self.assertTrue(validate_command_string('C 20 4'))

    def test_validate_input_args_with_correct_args(self):
        """Test to validate the input args validation with
        the correct number of arguments provided"""
        self.assertTrue(validate_input_args(["Q"]))
        self.assertTrue(validate_input_args(["C", 20, 5]))
        self.assertTrue(validate_input_args(['L', 1, 2, 3, 2]))
        self.assertTrue(validate_input_args(['R', 1, 2, 3, 4]))
        self.assertTrue(validate_input_args(['B', 1, 2, 'o']))

    def test_validate_input_args_with_wrong_number_of_args(self):
        """Test to validate the input args validation with
        the wrong number of arguments provided"""
        self.assertFalse(validate_input_args(['Q', 1]))
        self.assertFalse(validate_input_args(['C', 20]))
        self.assertFalse(validate_input_args(['L', 1, 2, 3]))
        self.assertFalse(validate_input_args(['R', 1, 2, 3]))
        self.assertFalse(validate_input_args(['B', 1]))

    def test_validate_file_name(self):
        """Test to validate that the filename is provided
        correctly"""
        input_str_1 = '.txt'
        input_str_2 = 'filename'
        input_str_3 = '1.tx'
        input_str_4 = ''
        input_str_5 = 'filename.txt'

        self.assertFalse(validate_file_name(input_str_1))
        self.assertFalse(validate_file_name(input_str_2))
        self.assertFalse(validate_file_name(input_str_3))
        self.assertFalse(validate_file_name(input_str_4))
        self.assertTrue(validate_file_name(input_str_5))


if __name__ == '__main__':
    unittest.main()
