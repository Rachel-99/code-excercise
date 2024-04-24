from src.input_layer.file_reader import FileReader
from src.input_layer.format_input_validator import FormatInputValidator
from src.input_layer.mapper import Mapper
from src.process_layer.attendance_usecase import AttendanceUseCase
from src.output_layer.file_writer import FileWriter

class Orchestrator:
    def __init__(self, log, file_reader: FileReader, format_input_validator: FormatInputValidator, 
                 mapper: Mapper, attendance_usecase: AttendanceUseCase, 
                 file_writer: FileWriter):
        self._file_reader = file_reader
        self._format_input_validator = format_input_validator
        self._log = log
        self._mapper = mapper
        self._attendance_usecase = attendance_usecase
        self._file_writer = file_writer
    
    def start(self, path):
        read_result = self._file_reader.read(path)
        if (read_result.has_error):
            self._log.error(read_result.error_message)
            return
        
        commands = read_result.content
        
        format_input_validator_result = self._format_input_validator.validate(commands)
        if (not format_input_validator_result.is_valid):
            self._log.error(f"Invalid command: {format_input_validator_result.invalid_command}")
            return

        student_commands, presence_commands = self.__group_commands_by_type(commands)
        students = self._mapper.map_student_commands_to_students_array(student_commands)
        presences = self._mapper.map_presence_commands_to_presence_objects(presence_commands)
        students_data = {'students': students, 'presences': presences}
        
        student_attendance_result = self._attendance_usecase.perform_operation(students_data)
        if (student_attendance_result.has_error):
            self._log.error(student_attendance_result.error_message)
            return
        
        time_per_student = student_attendance_result.content
        
        write_result = self._file_writer.write(time_per_student)
        if (write_result.has_error):
            self._log.error(write_result.error_message)
            return
        
        report_content = write_result.content
        self._log.info(report_content)
    
    def __group_commands_by_type(self, commands):
        student_commands = []
        presence_commands = []
        
        for command in commands:
            if (command.startswith("Student")):
                student_commands.append(command)
            else:
                presence_commands.append(command)
          
        return student_commands, presence_commands