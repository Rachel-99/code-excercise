class Result:
    def __init__(self, content="", has_error=False, error_message=""):
        self._content = content
        self._has_error = has_error
        self._error_message = error_message
    
    @property
    def content(self):
        return self._content
    
    @property
    def has_error(self):
        return self._has_error
    
    @property
    def error_message(self):
        return self._error_message
    
