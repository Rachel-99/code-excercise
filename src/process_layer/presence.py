class Presence:
    def __init__(self, student_name, day, start_time, end_time):
        self._student_name = student_name
        self._day = day
        self._start_time = start_time
        self._end_time = end_time
    
    @property
    def student_name(self):
        return self._student_name
    
    @property
    def day(self):
        return self._day
    
    @property
    def start_time(self):
        return self._start_time
 
    @property
    def end_time(self):
        return self._end_time
    
 
