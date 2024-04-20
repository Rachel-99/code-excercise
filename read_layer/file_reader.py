from abc import ABC, abstractmethod
from read_layer.format_input_validator import FormatInputValidator
from .logger import log

class FileReader(ABC):
    @abstractmethod
    def readFile(self):
        pass

class TXTFileReader(FileReader):
    def __init__(self, input_validator: FormatInputValidator):
        self.input_validator = input_validator
        
    def readFile(self, path):
        try:
            with open(path, 'r') as file:
                content = file.readlines()
        except OSError as e:
            log.error(f"An error has ocurred: {e}")
            return
        
        input_is_valid = self.input_validator.validate(content)
        if (input_is_valid):
            # se envia a capa de procesamiento?
            print(content)
        
