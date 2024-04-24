import unittest
from src.input_layer.format_input_validator import CommandInputValidator


class TestCommandInputValidator(unittest.TestCase):
    
    def test_validate_valid_command(self):
        valid_command = ["Student Marco", "Presence Marco 1 09:02 10:17 R100"]
        
        command_input_validator = CommandInputValidator()
        result = command_input_validator.validate(valid_command)
        
        self.assertTrue(result.is_valid)
        
    
    def test_validate_invalid_command(self):
        invalid_command = ["Teacher Robert"]
        
        command_input_validator = CommandInputValidator()
        result = command_input_validator.validate(invalid_command)
        
        self.assertFalse(result.is_valid)
        self.assertEqual(result.invalid_command, invalid_command[0])
    
