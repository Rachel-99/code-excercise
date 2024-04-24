from abc import ABC, abstractmethod
from ..process_layer.presence import Presence

class Mapper(ABC):
    
    @abstractmethod
    def map_student_commands_to_students_array(self):
        pass
    
    @abstractmethod
    def map_presence_commands_to_presence_objects(self):
        pass

class InputMapper(Mapper):
    
    def map_student_commands_to_students_array(self, student_commands):
        students = []
        for student_command in student_commands:
            student_command_components = student_command.split() 
            student = " ".join(student_command_components[1:])
            if (student not in students):
                students.append(student)
        
        return students
     
    def map_presence_commands_to_presence_objects(self, presence_commands):
        presences = []
        for presence_command in presence_commands:
            presence_command_components = presence_command.split()
            
            student_name = presence_command_components[1]
            attendance_day = presence_command_components[2]
            start_time = presence_command_components[3]
            end_time = presence_command_components[4]
            
            presence = Presence(student_name, attendance_day, start_time, end_time)
            presences.append(presence)
        
        return presences
            
