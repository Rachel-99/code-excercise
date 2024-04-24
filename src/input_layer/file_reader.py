from abc import ABC, abstractmethod
from ..process_layer.result import Result

class FileReader(ABC):
    @abstractmethod
    def read(self):
        pass

class TextFileReader(FileReader):
    def read(self, path):
        try:
            with open(path, 'r') as file:
                content = file.readlines()
            result = Result(content)
        except OSError as e:
            result = Result(has_error=True, error_message=str(e))
            
        return result
