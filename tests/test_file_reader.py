from src.input_layer.file_reader import TextFileReader
import unittest

class TestTextFileReader(unittest.TestCase):

    def test_read_open_file_error(self):
        path = 'this_file_doesnt_exist.txt'
        file_reader = TextFileReader()
        
        actual_result = file_reader.read(path)

        expected_result = f"[Errno 2] No such file or directory: '{path}'"
        self.assertTrue(actual_result.has_error)
        self.assertEqual(actual_result.error_message, expected_result)
        
    def test_read_open_file_success(self):
        path = 'tests/test_input.txt'
        file_reader = TextFileReader()
        
        actual_result = file_reader.read(path)
        
        expected_result = ["Teacher Robert"]
        self.assertFalse(actual_result.has_error)
        self.assertEqual(actual_result.content, expected_result)
        