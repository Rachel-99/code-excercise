from src.output_layer.file_writer import TextFileWriter
import unittest
from unittest.mock import patch

class TestTextFileWriter(unittest.TestCase):

    def test_write_file_error(self):
        file_writer = TextFileWriter()
        students_attendance = {"David": [225, 1], "Marco": [157, 2], "Marta": [0, 0], "Francisca": [0, 0]}
        
        with patch('builtins.open', side_effect=OSError('An error has ocurred')):
            result = file_writer.write(students_attendance)
            
        self.assertTrue(result.has_error)
        self.assertEqual(result.error_message, 'An error has ocurred')

        
    def test_write_file_success(self):
        students_attendance = {"David": [225, 1], "Marco": [157, 2], "Marta": [0, 0], "Francisca": [0, 0]}
        file_writer = TextFileWriter()
        
        actual_result = file_writer.write(students_attendance)
        
        expected_result = "David: 225 minutes in 1 day\nMarco: 157 minutes in 2 days\nMarta: 0 minutes\nFrancisca: 0 minutes\n"
        self.assertFalse(actual_result.has_error)
        self.assertEqual(actual_result.content, expected_result)
        