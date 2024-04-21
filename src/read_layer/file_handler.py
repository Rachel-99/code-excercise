from abc import ABC, abstractmethod
from .format_input_validator import FormatInputValidator

class FileHandler(ABC):
    @abstractmethod
    def execute(self):
        pass

class TextFileHandler(FileHandler):
    def __init__(self, input_validator: FormatInputValidator, log):
        self.input_validator = input_validator
        self.log = log
        
    def execute(self, path):
        try:
            with open(path, 'r') as file:
                content = file.readlines()
        except OSError as e:
            self.log.error(f"An error has ocurred: {e}")
            raise
        
        input_is_valid = self.input_validator.validate(content)
        if (input_is_valid):
            # se envia a capa de procesamiento
            print(content)
        else:
            self.log.error("Invalid input")
