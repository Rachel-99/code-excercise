import unittest
from unittest.mock import Mock, patch
from src.orchestrator.orchestrator import Orchestrator
from src.input_layer.file_reader import TextFileReader
from src.input_layer.format_input_validator import CommandInputValidator, ValidationResult
from src.input_layer.mapper import InputMapper
from src.process_layer.attendance_usecase import StudentAttendanceRecorderUseCase
from src.process_layer.result import Result
from src.output_layer.file_writer import TextFileWriter
from io import StringIO

class TestInputMapper(unittest.TestCase):
    
    def test_start_read_file_error(self):
        mock_logger = Mock()
        mock_text_file_reader = Mock(spec=TextFileReader)
        orchestrator = Orchestrator(mock_logger, mock_text_file_reader, None, None, None, None)
        mock_text_file_reader.read.return_value = Result(has_error=True, error_message="No such file or directory: 'example_file.txt'")
        
        orchestrator.start("example_file.txt")
        
        mock_text_file_reader.read.assert_called_once_with("example_file.txt")
        mock_logger.error.assert_called_once_with("No such file or directory: 'example_file.txt'")
        
    
    def test_start_invalid_commands(self):
        mock_logger = Mock()
        mock_command_input_validator = Mock(spec=CommandInputValidator)
        mock_text_file_reader = Mock(spec=TextFileReader)
        orchestrator = Orchestrator(mock_logger, mock_text_file_reader, mock_command_input_validator, None, None, None)
        
        mock_text_file_reader.read.return_value = Result(['Teacher Robert', 'Student Juan', 'Presence Marta 1 09:13 10:24 F201'])
        mock_command_input_validator.validate.return_value = ValidationResult(False, invalid_command="Teacher Robert")
        orchestrator.start("example_file.txt")
        
        mock_command_input_validator.validate.assert_called_once_with(['Teacher Robert', 'Student Juan', 'Presence Marta 1 09:13 10:24 F201'])
        mock_logger.error.assert_called_once_with(f"Invalid command: Teacher Robert")
        
    
    def test_start_unregistered_students_error(self):
        mock_logger = Mock()
        mock_command_input_validator = Mock(spec=CommandInputValidator)
        mock_text_file_reader = Mock(spec=TextFileReader)
        mock_input_mapper = Mock(spec=InputMapper)
        mock_student_attendance_recorder = Mock(spec=StudentAttendanceRecorderUseCase)
        orchestrator = Orchestrator(mock_logger, mock_text_file_reader, mock_command_input_validator, mock_input_mapper, mock_student_attendance_recorder, None)
        
        mock_text_file_reader.read.return_value = Result(['Student Robert', 'Student Juan', 'Presence Marta 1 09:13 10:24 F201'])
        mock_command_input_validator.validate.return_value = ValidationResult(True)
        mock_student_attendance_recorder.perform_operation.return_value = Result(has_error=True, error_message="The following students are not registered: ['Marta']")
        orchestrator.start("example_path.txt")
        
        #mock_student_attendance_recorder.perform_operation.assert_called_once_with()
        mock_logger.error.assert_called_once_with("The following students are not registered: ['Marta']")
    
    def test_start_write_report_error(self):
        mock_logger = Mock()
        mock_command_input_validator = Mock(spec=CommandInputValidator)
        mock_text_file_reader = Mock(spec=TextFileReader)
        mock_input_mapper = Mock(spec=InputMapper)
        mock_student_attendance_recorder = Mock(spec=StudentAttendanceRecorderUseCase)
        mock_text_file_writer = Mock(spec=TextFileWriter)
        orchestrator = Orchestrator(mock_logger, mock_text_file_reader, mock_command_input_validator, mock_input_mapper, mock_student_attendance_recorder, mock_text_file_writer)
        
        mock_text_file_reader.read.return_value = Result(['Student Robert', 'Student Juan', 'Presence Robert 1 09:13 10:24 F201'])
        mock_command_input_validator.validate.return_value = ValidationResult(True)
        mock_student_attendance_recorder.perform_operation.return_value = Result({"Robert": [71, 1], "Juan": [0, 0]})
        mock_text_file_writer.write.return_value = Result(has_error=True, error_message="Permision Denied")
        orchestrator.start("example_path.txt")
        
        mock_text_file_writer.write.assert_called_once_with({"Robert": [71, 1], "Juan": [0, 0]})
        mock_logger.error.assert_called_once_with("Permision Denied")
    
    def test_start_success(self):
        mock_logger = Mock()
        mock_command_input_validator = Mock(spec=CommandInputValidator)
        mock_text_file_reader = Mock(spec=TextFileReader)
        mock_input_mapper = Mock(spec=InputMapper)
        mock_student_attendance_recorder = Mock(spec=StudentAttendanceRecorderUseCase)
        mock_text_file_writer = Mock(spec=TextFileWriter)
        orchestrator = Orchestrator(mock_logger, mock_text_file_reader, mock_command_input_validator, mock_input_mapper, mock_student_attendance_recorder, mock_text_file_writer)
        mock_text_file_reader.read.return_value = Result(['Student Robert', 'Student Juan', 'Presence Robert 1 09:13 10:24 F201'])
        mock_command_input_validator.validate.return_value = ValidationResult(True)
        mock_student_attendance_recorder.perform_operation.return_value = Result({"Robert": [71, 1], "Juan": [0, 0]})
        mock_text_file_writer.write.return_value = Result("Robert: 71 minutes in 1 day\nJuan: 0 minutes")
        
        report_content = StringIO()
        with patch('sys.stdout', report_content):
            orchestrator.start("example_path.txt")
            
        report_content = report_content.getvalue()
        expected_output = "Robert: 71 minutes in 1 day\nJuan: 0 minutes\n"
        self.assertEqual(report_content, expected_output)