from read_layer.file_handler import TextFileHandler
from read_layer.format_input_validator import CommandInputValidator
import logging as log
import sys

log.basicConfig(level=log.DEBUG, 
                format='%(asctime)s: %(levelname)s [%(filename)s: line %(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('errors.log'),
                    log.StreamHandler()
])

if len(sys.argv) > 1:
    file_path = sys.argv[1]
    command_input_validator = CommandInputValidator(log)
    txt_file_handler = TextFileHandler(command_input_validator, log)
    txt_file_handler.execute(file_path)
    
else:
    log.error("No input recieved.")


    