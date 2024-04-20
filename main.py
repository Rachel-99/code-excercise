from read_layer.file_reader import TXTFileReader
from read_layer.format_input_validator import CommandInputValidator
from read_layer.logger import log

import sys

#python yourcode.py input.txt
# sys.argv: ['main.py', 'input.txt'] (son los path a cada archivo)

if len(sys.argv) > 1:
    file_path = sys.argv[1]
    command_input_validator = CommandInputValidator()
    txt_file_reader = TXTFileReader(command_input_validator)
    txt_file_reader.readFile(file_path)
    
else:
    log.error("No input recieved.")


    