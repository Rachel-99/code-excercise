import unittest
import unittest.mock
from src.read_layer.format_input_validator import CommandInputValidator


class TestCommandInputValidator(unittest.TestCase):
    
    def test_validate_valid_command(self):
        log_mock = unittest.mock.Mock()
        valid_command = ["Student Marco", "Presence Marco 1 09:02 10:17 R100"]
        
        command_input_validator = CommandInputValidator(log_mock)
        result = command_input_validator.validate(valid_command)
        
        self.assertEqual(result, True)
        
    
    def test_validate_invalid_command(self):
        log_mock = unittest.mock.Mock()
        invalid_command = ["invalid command"]
        
        command_input_validator = CommandInputValidator(log_mock)
        result = command_input_validator.validate(invalid_command)
        
        log_mock.error.assert_called_with(f'Invalid command: {invalid_command[0]}')
        self.assertEqual(result, False)
    
