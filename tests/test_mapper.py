from src.input_layer.mapper import InputMapper
from src.process_layer.presence import Presence
import unittest

class TestInputMapper(unittest.TestCase):

    def test_map_student_commands_to_students_array(self):
        student_commands = ['Student Marco', 'Student David', 'Student Marta', 'Student Francisca']
        
        input_mapper = InputMapper()
        actual_result = input_mapper.map_student_commands_to_students_array(student_commands)
        
        expected_result = ['Marco', 'David', 'Marta', 'Francisca']
        self.assertEqual(actual_result, expected_result)
    
    def test_map_presence_commands_to_presence_objects(self):
        presence_commands = ['Presence Marco 1 09:02 10:17 R100', 'Presence David 3 10:58 12:05 R205']
        
        input_mapper = InputMapper()
        presence_objects = input_mapper.map_presence_commands_to_presence_objects(presence_commands)
        
        self.assertEqual(len(presence_objects), 2)
        self.assertIsInstance(presence_objects[0], Presence) 
        self.assertEqual(presence_objects[0].student_name, "Marco")     
        self.assertEqual(presence_objects[0].day, "1")  
        self.assertEqual(presence_objects[0].start_time, "09:02")  
        self.assertEqual(presence_objects[0].end_time, "10:17")  
        
        self.assertEqual(presence_objects[1].student_name, "David")     
        self.assertEqual(presence_objects[1].day, "3")  
        self.assertEqual(presence_objects[1].start_time, "10:58")  
        self.assertEqual(presence_objects[1].end_time, "12:05")  
            