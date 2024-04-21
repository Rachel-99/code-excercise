from abc import ABC, abstractmethod
import re

class FormatInputValidator(ABC):
    @abstractmethod
    def validate(self):
        pass

class CommandInputValidator(FormatInputValidator):
    REGEX_STUDENT_COMMAND = re.compile(r'^Student\s[a-zA-Z]+$')
    REGEX_PRESENCE_COMMAND = re.compile(r'^Presence\s[a-zA-Z]+\s[1-7]\s(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]\s(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]\s[a-zA-Z0-9]+$')
    
    def __init__(self, log):
        self.log = log
        
    def validate(self, commands):
        print(commands)
        for command in commands:
            if (re.match(CommandInputValidator.REGEX_STUDENT_COMMAND, command)):
                continue
            elif (re.match(CommandInputValidator.REGEX_PRESENCE_COMMAND, command)):
                continue
            else:
                self.log.error(f'Invalid command: {command}')
                return False
        return True