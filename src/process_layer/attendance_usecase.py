from abc import ABC, abstractmethod
from datetime import datetime 
from collections import defaultdict
from ..process_layer.result import Result

class AttendanceUseCase(ABC):
    @abstractmethod
    def perform_operation(self):
        pass

class StudentAttendanceRecorderUseCase(AttendanceUseCase):   
    def perform_operation(self, students_data):
        registered_students = students_data['students']
        student_presences = students_data['presences']
        student_names_from_presences = [presence.student_name for presence in student_presences]
        are_all_students_registered = set(student_names_from_presences).issubset(set(registered_students))
        
        if (not are_all_students_registered):
            non_registered_students = list(set(student_names_from_presences) - set(registered_students))
            non_registered_students.sort()
            return Result(has_error=True, error_message=f"The following students are not registered: {non_registered_students}")
        
        students_attendance = self.__get_students_attendance(student_presences, registered_students)
        students_attendance_ordered_by_minutes = dict(sorted(students_attendance.items(), key=lambda x: x[1][0], reverse=True))

        return Result(students_attendance_ordered_by_minutes)
    
    def __get_students_attendance(self, student_presences, registered_students):
        total_minutes_attended = 0
        students_attendance = defaultdict(lambda: [total_minutes_attended, set()])
        
        for registered_student in registered_students:
            students_attendance[registered_student]

        for presence in student_presences:
            student_name = presence.student_name
            attendance_minutes = self.__calculate_attendance_minutes(presence)
            attendance_day = presence.day
            
            if (attendance_minutes < 5):
                students_attendance[student_name][0] += 0
            else:
                students_attendance[student_name][0] += attendance_minutes
                students_attendance[student_name][1].add(attendance_day)
            
        for student, attendance in students_attendance.items():
            minutes, days_set = attendance
            students_attendance[student] = [int(minutes), int(len(days_set))]
        
        return students_attendance
                    
    def __calculate_attendance_minutes(self, student_presence):
        start = datetime.strptime(student_presence.start_time, "%H:%M") 
        end = datetime.strptime(student_presence.end_time, "%H:%M") 
        
        difference = end - start 
        seconds = difference.total_seconds()         
        minutes = seconds / 60
        
        return minutes
    
    
    

    