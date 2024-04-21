import unittest
import unittest.mock
from src.read_layer.file_handler import TextFileHandler


class TestTextFileHandler(unittest.TestCase):
    
    def test_execute_open_file_error(self):
        format_input_validator_mock = unittest.mock.MagicMock()
        log_mock = unittest.mock.Mock()
        path = 'this_file_doesnt_exist.txt'
        
        txt_file_handler = TextFileHandler(format_input_validator_mock,log_mock)
        with self.assertRaises(OSError) as context:
            txt_file_handler.execute(path)
                
        log_mock.error.assert_called_once_with(f"An error has ocurred: {str(context.exception)}")

            
    def test_execute_invalid_commands(self):
        format_input_validator_mock = unittest.mock.MagicMock()
        log_mock = unittest.mock.MagicMock()
        format_input_validator_mock.validate.return_value = False
        path = 'tests/test_input.txt'
        
        txt_file_handler = TextFileHandler(format_input_validator_mock,log_mock)
        txt_file_handler.execute(path)
        
        format_input_validator_mock.validate.assert_called_once_with(["test content"])
        log_mock.error.assert_called_once_with('Invalid input')
    
    """
    def test_execute_valid_commands(self):
        pass
    """
    
        
        
        
        