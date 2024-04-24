from src.process_layer.attendance_usecase import StudentAttendanceRecorderUseCase
import unittest
from src.process_layer.presence import Presence

class TestStudentAttendanceRecorderUseCase(unittest.TestCase):
    
    def test_perform_operation_all_students_registered(self):
        registered_students = ['Marco', 'David', 'Marta', 'Francisca']
        presence_commands = [Presence('Marta', '1', '09:02', '09:04'), Presence('Marco', '3', '10:58', '12:05'), Presence('David', '5', '14:02', '15:46'), 
                             Presence('Marco', '4', '11:00', '12:30'), Presence('David', '5', '17:02', '19:03')]
        student_data = {'students': registered_students, 'presences': presence_commands}
        
        student_attendance_recorder = StudentAttendanceRecorderUseCase()
        actual_result = student_attendance_recorder.perform_operation(student_data)
        
        expected_result = {"David": [225, 1], "Marco": [157, 2], "Marta": [0, 0], "Francisca": [0, 0]}
        self.assertFalse(actual_result.has_error)
        self.assertEqual(actual_result.content, expected_result)
        
    def test_perform_operation_not_all_students_are_registered(self):
        registered_students = ['Marco', 'David', 'Marta', 'Francisca']
        presence_commands = [Presence('Javier', '1', '09:02', '10:17'), Presence('Marco', '3', '10:58', '12:05'), Presence('David', '5', '14:02', '15:46'), 
                             Presence('Juana', '4', '11:00', '12:30'), Presence('Pedro', '5', '17:02', '19:03')]
        student_data = {'students': registered_students, 'presences': presence_commands}
        
        student_attendance_recorder = StudentAttendanceRecorderUseCase()
        actual_result = student_attendance_recorder.perform_operation(student_data)
        
        expected_result = "The following students are not registered: ['Javier', 'Juana', 'Pedro']"
        self.assertTrue(actual_result.has_error)
        self.assertEqual(actual_result.error_message, expected_result)