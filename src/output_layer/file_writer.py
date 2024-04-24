from abc import ABC, abstractmethod
from src.process_layer.result import Result

class FileWriter(ABC):
    @abstractmethod
    def write(self):
        pass

class TextFileWriter(FileWriter):
    def write(self, students_attendance):
        file_content = self.__generate_report_content(students_attendance)
        
        try:
            with open("report.txt", "w") as report:
                report.write(file_content)
            result = Result(file_content)
        except OSError as e:
            result = Result(has_error=True, error_message=str(e))
            
        return result
    
    def __generate_report_content(self, students_attendance):
        file_content = ""
        
        for student, attendance in students_attendance.items():
            minutes, days_count = attendance
            if (minutes == 0):
                file_content += f"{student}: {minutes} minutes\n"
            else:
                day_or_days = "day" if days_count == 1 else "days"
                file_content += f"{student}: {minutes} minutes in {days_count} {day_or_days}\n"

        return file_content
    