from abc import ABC, abstractmethod
import re

class FormatInputValidator(ABC):
    @abstractmethod
    def validate(self):
        pass

class CommandInputValidator(FormatInputValidator):
    REGEX_STUDENT_COMMAND = re.compile(r'^Student\s[a-zA-Z]+$')
    REGEX_PRESENCE_COMMAND = re.compile(r'^Presence\s[a-zA-Z]+\s[1-7]\s(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]\s(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]\s[a-zA-Z0-9]+$')

    def validate(self, commands):
        for command in commands:
            if (re.match(CommandInputValidator.REGEX_STUDENT_COMMAND, command)):
                continue
            elif (re.match(CommandInputValidator.REGEX_PRESENCE_COMMAND, command)):
                continue
            else:
                return ValidationResult(False, invalid_command=command)
        return ValidationResult(True)

class ValidationResult:
    def __init__(self, is_valid, invalid_command=""):
        self._is_valid = is_valid
        self._invalid_command = invalid_command
    
    @property
    def is_valid(self):
        return self._is_valid
    
    @property
    def invalid_command(self):
        return self._invalid_command