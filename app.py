from src.orchestrator.orchestrator import Orchestrator
from src.input_layer.file_reader import TextFileReader
from src.input_layer.format_input_validator import CommandInputValidator
from src.input_layer.mapper import InputMapper
from src.process_layer.attendance_usecase import StudentAttendanceRecorderUseCase
from src.output_layer.file_writer import TextFileWriter
from logger import configure_logger

def build_app():
    logger = configure_logger()
    text_file_reader = TextFileReader()
    command_input_validator = CommandInputValidator()
    input_mapper = InputMapper()
    student_attendance_recorder = StudentAttendanceRecorderUseCase()
    text_file_writer = TextFileWriter()
    orchestrator = Orchestrator(logger, text_file_reader, command_input_validator,
                                input_mapper, student_attendance_recorder, text_file_writer)
    return orchestrator